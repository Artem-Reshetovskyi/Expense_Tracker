#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging

logger = logging.getLogger(__name__)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        logger.error("Django is not installed. Try running 'pip install -r requirements.txt'.")
        logger.debug("Detailed exception info: %s", exc, exc_info=True)

        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    try:
        execute_from_command_line(sys.argv)
    except KeyboardInterrupt:
        logger.warning("Execution interrupted by user (Ctrl+C).")
        sys.exit(0)
    except Exception as e:
        logger.exception("Unexpected error occurred:")
        sys.exit(1)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()