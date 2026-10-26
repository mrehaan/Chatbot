"""Settings used by the Django management-command chatbot."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "development-only-key-change-before-deployment"
DEBUG = True
ALLOWED_HOSTS: list[str] = []

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "chatbot",
]

MIDDLEWARE: list[str] = []
ROOT_URLCONF = "chatbot_project.urls"
TEMPLATES: list[dict] = []
WSGI_APPLICATION = "chatbot_project.wsgi.application"
ASGI_APPLICATION = "chatbot_project.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "django.sqlite3",
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/New_York"
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
