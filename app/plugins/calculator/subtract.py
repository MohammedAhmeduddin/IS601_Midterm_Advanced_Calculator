import logging
from app.commands import Command
from app.history_manager import HistoryManager

class Subtract(Command):
    def __init__(self):
        self.history_manager = HistoryManager()

    def execute(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            logging.info(f"Subtracting {num2} from {num1}: Result = {result}")
            print(f"The result of {num1} - {num2} is {result}")
            # Store the result in history
            self.history_manager.add_record("Subtract", num1, num2, result)
        except ValueError as e:
            logging.error(f"Invalid input for subtraction: {e}")
            print("Error: Please enter valid numbers.")
