import sys
import logging
from app.commands import Command, CommandHandler

class MenuCommand(Command):
    """
    Command to display a dynamic menu of available commands and execute the selected command.

    Attributes:
        command_handler (CommandHandler): Manages the list of registered commands and their execution.
    """

    def __init__(self, command_handler: CommandHandler):
        """
        Initializes the MenuCommand with a reference to the CommandHandler.

        Args:
            command_handler (CommandHandler): The handler that manages available commands.
        """
        self.command_handler = command_handler

    def execute(self):
        """
        Executes the menu command, displaying a list of registered commands for user selection.

        Prompts the user to select a command by number or exit by selecting '0'. Handles
        errors like invalid input, out-of-range selections, and unexpected exceptions.
        """
        commands = list(self.command_handler.commands.keys())

        # Display the menu
        print("\nMain Menu:")
        for index, command_name in enumerate(commands, start=1):
            print(f"{index}. {command_name.capitalize()}")
        print("Enter the number of the command to execute, or '0' to exit.")

        try:
            # EAFP: Assume input can be converted to integer and is within range
            selection = int(input("Selection: "))
            if selection == 0:
                logging.info("User selected to exit the program.")
                sys.exit("Exiting program.")  # Exit if the user selects '0'

            # Attempt to retrieve and execute the command
            command_name = commands[selection - 1]  # Adjust for zero-based indexing
            logging.info(f"User selected command: {command_name}")
            self.command_handler.execute_command(command_name)

        except ValueError:
            # Handle non-numeric input
            logging.warning("Invalid input: non-numeric selection entered.")
            print("Invalid selection. Please enter a valid number.")
        except IndexError:
            # Handle selection out of range
            logging.warning(f"Invalid selection: {selection} is out of range.")
            print("Invalid selection. Please enter a valid number.")
        except KeyError:
            # Handle command not found
            logging.error(f"Command '{command_name}' could not be executed.")
            print("Selected command could not be executed.")
        except SystemExit:
            # Allow SystemExit for graceful program termination
            logging.info("System exit initiated.")
            raise
        except Exception as e:
            # Handle any other unexpected errors
            logging.error(f"Unexpected error occurred: {e}")
            print("An unexpected error occurred. Please try again.")
