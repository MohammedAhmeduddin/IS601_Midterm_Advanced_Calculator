import pkgutil
import importlib
import logging
from app.commands import Command

class CalculatorCommand(Command):
    def __init__(self, plugins_package='app.plugins.calculator'):
        """Initialize the calculator by dynamically loading operations from the specified plugins package."""
        self.plugins_package = plugins_package
        self.operations = self.load_operations()
        logging.info(f"Calculator operations initialized with {len(self.operations)} operations.")

    def load_operations(self):
        """Dynamically loads available calculator operation plugins."""
        operations = {}
        plugin_paths = [self.plugins_package.replace('.', '/')]
        found_plugins = pkgutil.iter_modules(plugin_paths)
        
        # Sort plugins by name to ensure consistent order
        sorted_plugins = sorted(found_plugins, key=lambda x: x[1])

        for index, (finder, name, ispkg) in enumerate(sorted_plugins, start=1):
            if ispkg:
                continue  # Skip sub-packages
            try:
                # Dynamically import the plugin module
                plugin_module = importlib.import_module(f"{self.plugins_package}.{name}")
                # Register the plugin commands
                self.register_operations(plugin_module, name, index, operations)
            except ImportError as e:
                logging.error(f"Error importing plugin {name}: {e}")
            except Exception as e:
                logging.error(f"Unexpected error while loading plugin {name}: {e}")

        logging.info(f"Loaded operations: {list(operations.keys())}")
        return operations

    def register_operations(self, plugin_module, name, index, operations):
        """Registers operations from a plugin module."""
        try:
            for attribute_name in dir(plugin_module):
                attribute = getattr(plugin_module, attribute_name)
                # Ensure the attribute is a class and a valid Command subclass
                if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                    operations[str(index)] = attribute()
                    logging.info(f"Registered operation: {name} as {attribute_name} with index {index}")
        except TypeError as e:
            logging.error(f"Error registering operation {name}: {e}")

    def display_menu(self):
        """Displays the list of available calculator operations."""
        print("\nCalculator Operations:")
        # Ensure menu items are displayed in order
        for key in sorted(self.operations.keys(), key=int):
            print(f"{key}. {self.operations[key].__class__.__name__}")
        print("0. Back")

    def execute(self):
        """Executes the calculator command, prompting user for operation selection."""
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
