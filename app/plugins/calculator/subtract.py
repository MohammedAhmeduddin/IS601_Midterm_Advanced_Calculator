import logging
from app.commands import Command

class Subtract(Command):
    def execute(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            logging.info(f"Subtracting {num2} from {num1}: Result = {result}")
            print(f"The result of {num1} - {num2} is {result}")
        except ValueError as e:
            logging.error(f"Invalid input for subtraction: {e}")
            print("Error: Please enter valid numbers.")
