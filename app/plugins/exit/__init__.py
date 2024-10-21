import sys
import logging
from app.commands import Command

class ExitCommand(Command):
    def execute(self):
        try:
            logging.info("ExitCommand executed: Application is exiting.")
            sys.exit("Exiting...")
        except SystemExit as e:
            logging.info(f"System exit with message: {e}")
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred while exiting: {e}")
