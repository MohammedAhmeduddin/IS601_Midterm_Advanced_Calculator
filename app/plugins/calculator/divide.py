import logging
from app.commands import Command

class Divide(Command):
    def execute(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                logging.error("Division by zero attempted.")
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                logging.info(f"Dividing {num1} by {num2}: Result = {result}")
                print(f"The result of {num1} / {num2} is {result}")
        except ValueError as e:
            logging.error(f"Invalid input for division: {e}")
            print("Error: Please enter valid numbers.")
