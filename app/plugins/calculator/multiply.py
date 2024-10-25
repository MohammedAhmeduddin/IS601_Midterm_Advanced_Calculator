import logging
from app.commands import Command
from app.history_manager import HistoryManager

class Multiply(Command):
    """
    Command to perform a multiplication operation between two numbers.

    Attributes:
        history_manager (HistoryManager): Manages the history of calculation records.
    """

    def __init__(self):
        """
        Initializes the Multiply command with a history manager to log the operation's result.
        """
        self.history_manager = HistoryManager()

    def execute(self):
        """
        Executes the multiplication operation by prompting the user for two numbers.

        Prompts the user to input two numbers, calculates their product, displays the result,
        logs the operation, and stores it in the history. Handles invalid input with an error message.

        Raises:
            ValueError: If the input is not a valid number.
        """
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            logging.info(f"Multiplying {num1} and {num2}: Result = {result}")
            print(f"The result of {num1} * {num2} is {result}")
            # Store the result in history
            self.history_manager.add_record("Multiply", num1, num2, result)
        except ValueError as e:
            logging.error(f"Invalid input for multiplication: {e}")
            print("Error: Please enter valid numbers.")
