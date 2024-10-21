import os
import pkgutil
import importlib
import sys
from app.commands import CommandHandler, Command
from app.plugins.menu import MenuCommand
from dotenv import load_dotenv  # type: ignore
import logging
import logging.config

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
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
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def print_main_menu(self):
        logging.info("Displaying main menu.")
        print("\nAvailable commands:")
        self.command_handler.list_commands()
        print("Type the number of the command to execute, or type 'exit' to exit.")

    def start(self):
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


