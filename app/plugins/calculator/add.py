import logging
from app.commands import Command

class Add(Command):
    def execute(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            logging.info(f"Adding {num1} and {num2}: Result = {result}")
            print(f"The result of {num1} + {num2} is {result}")
        except ValueError as e:
            logging.error(f"Invalid input for addition: {e}")
            print("Error: Please enter valid numbers.")

