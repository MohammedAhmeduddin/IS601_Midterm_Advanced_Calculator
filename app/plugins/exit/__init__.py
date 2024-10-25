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
        
        Raises:
            SystemExit: Terminates the program with an exit message.
        """
        try:
            logging.info("ExitCommand executed: Application is exiting.")
            sys.exit("Exiting...")
        except SystemExit as e:
            logging.info(f"System exit with message: {e}")
            raise  # Re-raise the SystemExit to allow graceful shutdown
        except Exception as e:
            logging.error(f"An unexpected error occurred while exiting: {e}")
