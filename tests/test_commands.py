"""
Unit tests for various commands within the App, including REPL handling for greet, menu, and calculator commands.
"""

from unittest.mock import MagicMock
import sys
import pytest
from app.commands import Command, CommandHandler
from app import App
from app.plugins.calculator import CalculatorCommand
from app.plugins.menu import MenuCommand


def test_app_greet_command(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch):
    """
    Test that the REPL correctly handles the 'greet' command.

    Simulates the user selecting the 'greet' command and then exiting the REPL.
    Verifies that "Hello, World!" is output and the application exits cleanly.
    """
    inputs = iter(['3', 'exit'])  # Assuming '3' selects the greet command
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()

    captured = capfd.readouterr()
    assert "Hello, World!" in captured.out
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 0


def test_app_menu_command(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch):
    """
    Test that the REPL correctly handles the 'menu' command.

    Simulates the user entering 'menu' and then 'exit', verifying that the menu is displayed.
    """
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "Available commands:" in captured.out


class MockAddCommand(Command):
    """Mock command for addition operation."""
    def execute(self):
        print("Performing addition")

class MockSubtractCommand(Command):
    """Mock command for subtraction operation."""
    def execute(self):
        print("Performing subtraction")


@pytest.fixture
def mock_operations(monkeypatch: pytest.MonkeyPatch):
    """
    Fixture to mock the load_operations method in CalculatorCommand, simulating mock operations.
    """
    def mock_load_operations(self):
        return {'1': MockAddCommand(), '2': MockSubtractCommand()}
    monkeypatch.setattr(CalculatorCommand, "load_operations", mock_load_operations)


def test_calculator_display_operations_and_exit(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch, mock_operations: None):
    """
    Test that the CalculatorCommand displays available operations and exits properly.

    Verifies the presence of mock operations in the displayed menu and tests exiting.
    """
    monkeypatch.setattr('builtins.input', lambda _: '0')
    calculator_cmd = CalculatorCommand()
    calculator_cmd.execute()

    captured = capfd.readouterr()
    assert "\nCalculator Operations:" in captured.out
    assert "1. MockAddCommand" in captured.out
    assert "2. MockSubtractCommand" in captured.out
    assert "0. Back" in captured.out


def test_calculator_execute_operation(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch):
    """
    Test that the CalculatorCommand executes an operation based on user input.

    Simulates user input to select and execute an operation in the calculator.
    """
    inputs = ['1', '2', '3', '0']
    input_generator = (input for input in inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_generator))

    calculator_cmd = CalculatorCommand()
    calculator_cmd.execute()

    captured = capfd.readouterr()
    assert "The result of 2.0 + 3.0 is 5.0" in captured.out


class MockCommand(Command):
    """Mock command for general testing."""
    def execute(self):
        print("Mock command executed.")


@pytest.fixture
def command_handler_with_commands():
    """
    Fixture for a CommandHandler pre-populated with mock commands.
    Registers 'test' and 'help' commands in the handler.
    """
    handler = CommandHandler()
    handler.register_command('test', MockCommand())
    handler.register_command('help', MockCommand())
    return handler


def test_menu_command_display_and_exit(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch, command_handler_with_commands: CommandHandler):
    """
    Test that the MenuCommand displays the main menu and exits properly.

    Verifies that the main menu is displayed with registered commands, and that
    the application exits cleanly when '0' is selected.
    """
    monkeypatch.setattr('builtins.input', lambda _: '0')
    mock_exit = MagicMock()
    monkeypatch.setattr(sys, 'exit', mock_exit)
    menu_cmd = MenuCommand(command_handler_with_commands)
    menu_cmd.execute()

    captured = capfd.readouterr()
    assert "\nMain Menu:" in captured.out
    assert "1. Test" in captured.out
    assert "2. Help" in captured.out
    assert "Enter the number of the command to execute, or '0' to exit." in captured.out
    mock_exit.assert_called_once_with("Exiting program.")


def test_menu_command_invalid_selection(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch, command_handler_with_commands: CommandHandler):
    """
    Test that the MenuCommand handles invalid selections correctly.

    Simulates a user entering an invalid selection and verifies the appropriate error message.
    """
    inputs = iter(['999', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr(sys, 'exit', MagicMock())
    menu_cmd = MenuCommand(command_handler_with_commands)
    menu_cmd.execute()

    captured = capfd.readouterr()
    assert "Invalid selection. Please enter a valid number." in captured.out
