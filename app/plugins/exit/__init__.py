import sys
import logging
from app.commands import Command

class ExitCommand(Command):
    """
    Command to terminate the application.

    The command logs the exit attempt, then gracefully shuts down the application.
    """

    def execute(self):
        """
        Executes the exit command to terminate the application.

        Logs the exit event, triggers a system exit, and handles the SystemExit exception.
        """
        try:
            logging.info("ExitCommand executed: Application is exiting.")
            sys.exit("Exiting...")
        except SystemExit as e:
            # EAFP: Handle the expected SystemExit to log and re-raise for a graceful shutdown
            logging.info(f"System exit with message: {e}")
            raise  # Re-raise to ensure the application terminates
        except Exception as e:
            # Catch any other unexpected exceptions
            logging.error(f"An unexpected error occurred while exiting: {e}")
