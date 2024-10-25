# __init__.py (in calculator plugin)

import pkgutil
import importlib
import logging
from app.commands import Command

class CalculatorCommand(Command):
    """
    The CalculatorCommand class dynamically loads and manages calculator operations as plugins.
    
    Attributes:
        plugins_package (str): The package where calculator operation plugins are stored.
        operations (dict): A dictionary mapping operation indices to Command instances.
    """

    def __init__(self, plugins_package='app.plugins.calculator'):
        """
        Initialize the calculator by dynamically loading operations from the specified plugins package.

        Args:
            plugins_package (str): The package path where plugin modules for operations are located.
        """
        self.plugins_package = plugins_package
        self.operations = self.load_operations()
        logging.info(f"Calculator operations initialized with {len(self.operations)} operations.")

    def load_operations(self):
        """
        Dynamically loads available calculator operation plugins from the plugins package.

        Returns:
            dict: A dictionary mapping operation indices to Command instances.
        """
        operations = {}
        plugin_paths = [self.plugins_package.replace('.', '/')]
        found_plugins = pkgutil.iter_modules(plugin_paths)

        # Sort plugins by name to ensure consistent order
        sorted_plugins = sorted(found_plugins, key=lambda x: x[1])

        index = 1  # Start indexing at 1
        for finder, name, ispkg in sorted_plugins:
            if ispkg:
                continue  # Skip sub-packages
            try:
                # Dynamically import the plugin module
                plugin_module = importlib.import_module(f"{self.plugins_package}.{name}")
                # Register the plugin commands
                index = self.register_operations(plugin_module, name, index, operations)
            except ImportError as e:
                logging.error(f"Error importing plugin {name}: {e}")
            except Exception as e:
                logging.error(f"Unexpected error while loading plugin {name}: {e}")

        logging.info(f"Loaded operations: {list(operations.keys())}")
        return operations

    def register_operations(self, plugin_module, name, index, operations):
        """
        Registers operations from a plugin module.

        Args:
            plugin_module (module): The module containing the operation class.
            name (str): The name of the module.
            index (int): The current index to assign to the operation.
            operations (dict): The dictionary to store the operations.

        Returns:
            int: The updated index after registering the operations in the module.
        """
        try:
            for attribute_name in dir(plugin_module):
                attribute = getattr(plugin_module, attribute_name)
                # Ensure the attribute is a class and a valid Command subclass
                if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                    operations[str(index)] = attribute()
                    logging.info(f"Registered operation: {name} as {attribute_name} with index {index}")
                    index += 1  # Increment index for the next command
        except TypeError as e:
            logging.error(f"Error registering operation {name}: {e}")
        return index  # Return the updated index

    def display_menu(self):
        """
        Displays the list of available calculator operations in a user-friendly menu format.
        """
        print("\nCalculator Operations:")
        # Ensure menu items are displayed in order
        for key in sorted(self.operations.keys(), key=int):
            print(f"{key}. {self.operations[key].__class__.__name__}")
        print("0. Back")

    def execute(self):
        """
        Executes the calculator command, presenting a menu to the user for operation selection.
        
        Prompts the user to select an operation, executes the selected operation, 
        or exits to the main menu if '0' is selected. Logs each operation execution 
        and handles potential errors.
        """
        while True:
            self.display_menu()

            choice = input("Select an operation: ").strip()
            if choice == '0':
                logging.info("Exiting calculator menu.")
                break  # Exit to the main menu

            operation = self.operations.get(choice)
            if operation:
                try:
                    logging.info(f"Executing operation: {operation.__class__.__name__}")
                    operation.execute()  # Execute the selected operation
                except Exception as e:
                    logging.error(f"Error executing operation {operation.__class__.__name__}: {e}")
                    print(f"An error occurred: {e}")
            else:
                logging.warning(f"Invalid operation selection: {choice}")
                print("Invalid selection. Please try again.")
