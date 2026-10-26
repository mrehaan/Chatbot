#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""

import os
import sys


def main():
    """Run Django management commands."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatbot_project.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as error:
        raise ImportError(
            "Django is not installed. Run 'python3 -m pip install -r requirements.txt'."
        ) from error

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
