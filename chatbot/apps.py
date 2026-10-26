"""Django application configuration."""

from django.apps import AppConfig


class ChatbotConfig(AppConfig):
    """Configure the terminal chatbot Django application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "chatbot"
