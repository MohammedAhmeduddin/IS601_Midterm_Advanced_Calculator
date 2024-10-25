import logging
from app.commands import Command
from app.history_manager import HistoryManager

class Divide(Command):
    def __init__(self):
        self.history_manager = HistoryManager()

    def execute(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            result = num1 / num2
            logging.info(f"Dividing {num1} by {num2}: Result = {result}")
            print(f"The result of {num1} / {num2} is {result}")
            # Store the result in history
            self.history_manager.add_record("Divide", num1, num2, result)
        except ValueError as e:
            logging.error(f"Invalid input for division: {e}")
            print("Error:", e)
