import logging
from app.commands import Command
from app.history_manager import HistoryManager

class Subtract(Command):
    """
    Command to perform a subtraction operation between two numbers.

    Attributes:
        history_manager (HistoryManager): Manages the history of calculation records.
    """

    def __init__(self):
        """
        Initializes the Subtract command with a history manager to log the operation's result.
        """
        self.history_manager = HistoryManager()

    def execute(self):
        """
        Executes the subtraction operation by prompting the user for two numbers.

        Prompts the user to input two numbers, calculates their difference, displays the result,
        logs the operation, and stores it in the history. Handles invalid input with an error message.
        """
        try:
            # EAFP: Assume inputs are valid numbers and proceed with subtraction
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            logging.info(f"Subtracting {num2} from {num1}: Result = {result}")
            print(f"The result of {num1} - {num2} is {result}")
            # Store the result in history
            self.history_manager.add_record("Subtract", num1, num2, result)
        except ValueError as e:
            # Handle invalid input where conversion to float fails
            logging.error(f"Invalid input for subtraction: {e}")
            print("Error: Please enter valid numbers.")
