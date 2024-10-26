import logging
from app.commands import Command
from app.history_manager import HistoryManager

class Divide(Command):
    """
    Command to perform a division operation between two numbers.

    Attributes:
        history_manager (HistoryManager): Manages the history of calculation records.
    """

    def __init__(self):
        """
        Initializes the Divide command with a history manager to log the operation's result.
        """
        self.history_manager = HistoryManager()

    def execute(self):
        """
        Executes the division operation by prompting the user for two numbers.

        Prompts the user to input two numbers, attempts to perform the division, 
        displays the result, logs the operation, and stores it in the history. 
        Handles invalid input and division by zero with error messages.
        """
        try:
            # EAFP: Assume inputs are valid numbers and that division can proceed
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = num1 / num2
            logging.info(f"Dividing {num1} by {num2}: Result = {result}")
            print(f"The result of {num1} / {num2} is {result}")
            # Store the result in history
            self.history_manager.add_record("Divide", num1, num2, result)

        except ValueError as e:
            # Handle cases where inputs are not valid numbers
            logging.error(f"Invalid input for division: {e}")
            print("Error: Please enter valid numbers.")
        except ZeroDivisionError:
            # Handle division by zero specifically
            logging.error("Attempted division by zero.")
            print("Error: Cannot divide by zero.")
