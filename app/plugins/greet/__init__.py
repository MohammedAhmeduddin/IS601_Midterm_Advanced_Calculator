import logging
from app.commands import Command

class GreetCommand(Command):
    """
    Command to display a greeting message.

    This command logs and prints a simple "Hello, World!" message to the console.
    """

    def execute(self):
        """
        Executes the greet command, logging and displaying a greeting message.
        """
        try:
            # EAFP: Assume logging will succeed, handle unexpected issues
            logging.info("Hello, World!")
        except Exception as e:
            logging.error(f"Failed to log greeting message: {e}")

        try:
            # EAFP: Assume print will succeed, handle unexpected issues
            print("Hello, World!")
        except Exception as e:
            logging.error(f"Failed to print greeting message: {e}")
