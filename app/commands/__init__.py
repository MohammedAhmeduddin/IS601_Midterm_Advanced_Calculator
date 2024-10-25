from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract base class representing a command. 
    Classes inheriting from Command must implement the `execute` method.
    """

    @abstractmethod
    def execute(self):
        """
        Execute the command.
        This method should be overridden by subclasses to define specific command actions.
        """
        pass


class CommandHandler:
    """
    A handler for managing and executing commands.
    
    Attributes:
        commands (dict): A dictionary mapping command names to their corresponding Command instances.
    """

    def __init__(self):
        """
        Initializes a CommandHandler instance with an empty dictionary of commands.
        """
        self.commands = {}

    def register_command(self, command_name: str, command_instance: Command):
        """
        Registers a command with a given name.

        Args:
            command_name (str): The name of the command to register.
            command_instance (Command): An instance of a class inheriting from Command.
        """
        self.commands[command_name] = command_instance

    def execute_command(self, command_name: str):
        """
        Executes a command by its name.

        Args:
            command_name (str): The name of the command to execute.
        
        Raises:
            KeyError: If the command name is not found in the registered commands.
        """
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")

    def list_commands(self):
        """
        Prints a list of all registered command names with their respective indices.
        """
        for index, command_name in enumerate(self.commands, start=1):
            print(f"{index}. {command_name}")

    def get_command_by_index(self, index: int):
        """
        Retrieves the command name by its index in the command list.

        Args:
            index (int): The index of the command to retrieve.
        
        Returns:
            str or None: The command name if it exists at the given index; None otherwise.
        """
        try:
            command_name = list(self.commands.keys())[index]
            return command_name
        except IndexError:
            return None
