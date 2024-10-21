import sys
import logging
from app.commands import Command, CommandHandler

class MenuCommand(Command):
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def execute(self):
        commands = list(self.command_handler.commands.keys())
        # Print the menu dynamically based on registered commands
        print("\nMain Menu:")
        for index, command_name in enumerate(commands, start=1):
            print(f"{index}. {command_name.capitalize()}")
        print("Enter the number of the command to execute, or '0' to exit.")

        try:
            selection = int(input("Selection: "))
            if selection == 0:
                logging.info("User selected to exit the program.")
                sys.exit("Exiting program.")  # Gracefully exit if the user selects '0'
            command_name = commands[selection - 1]  # Adjust for zero-based indexing
            logging.info(f"User selected command: {command_name}")
            self.command_handler.execute_command(command_name)
        except ValueError:
            logging.warning("Invalid input: non-numeric selection entered.")
            print("Invalid selection. Please enter a valid number.")
        except IndexError:
            logging.warning(f"Invalid selection: {selection} is out of range.")
            print("Invalid selection. Please enter a valid number.")
        except KeyError:
            logging.error(f"KeyError: Command '{command_name}' could not be executed.")
            print("Selected command could not be executed.")
        except SystemExit:
            logging.info("System exit initiated.")
            raise
        except Exception as e:
            logging.error(f"Unexpected error occurred: {e}")
            print("An unexpected error occurred. Please try again.")
