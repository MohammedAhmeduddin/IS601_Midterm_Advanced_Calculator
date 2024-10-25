import os
import pkgutil
import importlib
import sys
from app.commands import CommandHandler, Command
from app.plugins.menu import MenuCommand
from dotenv import load_dotenv
import logging
import logging.config

# Import the new history commands
from app.plugins.calculator.history_commands import ShowHistory, ClearHistory, DeleteSpecificRecord

class App:
    """
    Main application class that manages configuration, environment settings, command loading, 
    and the main interactive loop.

    Attributes:
        settings (dict): A dictionary of environment variables.
        command_handler (CommandHandler): Handles registration and execution of commands.
    """

    def __init__(self):
        """
        Initializes the App instance, sets up logging, loads environment variables, 
        and initializes the command handler.
        """
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        """
        Configures logging for the application based on a logging configuration file.
        If the file is not found, a default logging configuration is used.
        """
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """
        Loads environment variables from a .env file and returns them as a dictionary.

        Returns:
            dict: A dictionary of environment variables.
        """
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        """
        Retrieves a specific environment variable from the settings dictionary.

        Args:
            env_var (str): The name of the environment variable to retrieve.

        Returns:
            str or None: The value of the environment variable, or None if it does not exist.
        """
        return self.settings.get(env_var, None)

    def load_plugins(self):
        """
        Dynamically loads and registers command plugins from the specified plugins directory.
        
        This method iterates over plugins, importing each and registering their commands. It 
        also registers specific history commands and a menu command for user interaction.
        """
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg and plugin_name != "menu":
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

        # Manually register the menu command, as it needs access to all registered commands
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        logging.info("Menu command registered.")

    def register_plugin_commands(self, plugin_module, plugin_name):
        """
        Registers all command classes from a plugin module with the command handler.

        Args:
            plugin_module (module): The module containing the command classes.
            plugin_name (str): The name of the plugin module.
        """
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def print_main_menu(self):
        """
        Prints the main menu, listing all available commands for user selection.
        """
        logging.info("Displaying main menu.")
        print("\nAvailable commands:")
        self.command_handler.list_commands()
        print("Type the number of the command to execute, or type 'exit' to exit.")

    def start(self):
        """
        Starts the application, loading plugins, displaying the main menu, and entering the 
        main interactive loop to handle user input for command selection.

        The loop allows users to select commands by number, handles invalid input, 
        and exits gracefully on 'exit' or keyboard interruption.
        
        Raises:
            SystemExit: If the user chooses to exit the application.
        """
        self.load_plugins()
        self.print_main_menu()
        logging.info("Application started. Type 'exit' to exit.")
        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    logging.info("Exiting application.")
                    sys.exit(0)
                try:
                    index = int(cmd_input) - 1
                    if index < 0:
                        self.print_main_menu()
                        continue
                    command_name = self.command_handler.get_command_by_index(index)
                    if command_name:
                        self.command_handler.execute_command(command_name)
                        logging.info(f"Executed command: {command_name}")
                        self.print_main_menu()
                    else:
                        logging.error("Invalid command selection.")
                        print("Invalid selection. Please enter a valid number.")
                except ValueError:
                    logging.error("Non-numeric input received.")
                    print("Only numbers are allowed, wrong input.")
        except KeyboardInterrupt:
            logging.info("Application interrupted by user. Exiting.")
            sys.exit(0)
        finally:
            logging.info("Application shutdown.")
