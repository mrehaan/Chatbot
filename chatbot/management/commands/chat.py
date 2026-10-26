"""Run the interactive ChatterBot terminal client."""

from pathlib import Path

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from chatbot.training_data import TRAINING_CONVERSATIONS

EXIT_WORDS = {"exit", "quit", "bye"}


class Command(BaseCommand):
    """Start an interactive terminal conversation with the trained chatbot."""

    help = "Start a terminal Q&A conversation with the ChatterBot assistant."

    def add_arguments(self, parser):
        parser.add_argument(
            "--no-train",
            action="store_true",
            help="Start without loading the included training conversations.",
        )

    def handle(self, *args, **options):
        bot = self._create_bot()

        if not options["no_train"]:
            self.stdout.write("Loading the training conversations...")
            trainer = ListTrainer(bot)
            for conversation in TRAINING_CONVERSATIONS:
                trainer.train(conversation)

        self.stdout.write(self.style.SUCCESS("Chatbot is ready. Type 'exit' to end the chat."))

        while True:
            try:
                user_message = input("user: ").strip()
            except (EOFError, KeyboardInterrupt):
                self.stdout.write("\nChat ended.")
                break

            if not user_message:
                self.stdout.write("bot: Please enter a question so I can respond.")
                continue

            if user_message.casefold() in EXIT_WORDS:
                self.stdout.write("bot: Goodbye. Thanks for chatting.")
                break

            try:
                response = bot.get_response(user_message)
            except Exception as error:
                raise CommandError(f"The chatbot could not create a response: {error}") from error

            self.stdout.write(f"bot: {response}")

    def _create_bot(self):
        """Create a bot whose ChatterBot data is stored inside this project."""
        database_path = Path(settings.BASE_DIR) / "data" / "chatbot.sqlite3"
        database_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            return ChatBot(
                "Assignment Q&A Bot",
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri=f"sqlite:///{database_path}",
                logic_adapters=[
                    {
                        "import_path": "chatterbot.logic.BestMatch",
                        "default_response": "I do not have an answer for that yet. Please ask about Python, Django, ChatterBot, or the greeting example.",
                        "maximum_similarity_threshold": 0.90,
                    }
                ],
                read_only=True,
            )
        except Exception as error:
            raise CommandError(
                "ChatterBot could not start. Install the project dependencies with "
                "'python3 -m pip install -r requirements.txt'. "
                f"Details: {error}"
            ) from error
