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
        logging.info("Hello, World!")
        print("Hello, World!")
