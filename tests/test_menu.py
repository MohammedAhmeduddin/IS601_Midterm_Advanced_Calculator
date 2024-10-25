"""
Test suite for MenuCommand class, which handles displaying and executing
commands from a dynamic menu interface.
"""

from unittest.mock import patch, MagicMock
import pytest
from app.plugins.menu import MenuCommand
from app.commands import CommandHandler

@pytest.fixture
def command_handler():
    """Fixture to set up a CommandHandler with mock commands."""
    handler = CommandHandler()
    handler.commands = {
        'greet': MagicMock(name='greet_command'),
        'exit': MagicMock(name='exit_command')
    }
    return handler

@pytest.fixture
def menu_command(command_handler):
    """Fixture to create a MenuCommand instance."""
    return MenuCommand(command_handler=command_handler)

def test_display_menu(menu_command, capsys):
    """Test that the menu displays all available commands correctly."""
    with patch("builtins.input", side_effect=["0"]):  # Simulate exit input
        with pytest.raises(SystemExit):
            menu_command.execute()
        captured = capsys.readouterr()
        assert "Main Menu:" in captured.out
        assert "1. Greet" in captured.out
        assert "2. Exit" in captured.out
        assert "Enter the number of the command to execute, or '0' to exit." in captured.out

def test_execute_valid_command(menu_command, command_handler):
    """Test executing a valid command from the menu."""
    with patch("builtins.input", side_effect=["1"]):  # Select 'greet' command
        menu_command.execute()
        command_handler.commands['greet'].execute.assert_called_once()

def test_execute_exit_command(menu_command):
    """Test selecting the exit option to terminate the program."""
    with patch("builtins.input", side_effect=["0"]), pytest.raises(SystemExit):
        menu_command.execute()

def test_invalid_input_non_numeric(menu_command, capsys):
    """Test handling of a non-numeric input."""
    with patch("builtins.input", side_effect=["abc"]):  # Simulate non-numeric input
        menu_command.execute()
        captured = capsys.readouterr()
        assert "Invalid selection. Please enter a valid number." in captured.out

def test_invalid_input_out_of_range(menu_command, capsys):
    """Test handling of a numeric input that's out of the command range."""
    with patch("builtins.input", side_effect=["3"]):  # Input outside valid range
        menu_command.execute()
        captured = capsys.readouterr()
        assert "Invalid selection. Please enter a valid number." in captured.out

def test_key_error_handling(menu_command, capsys, command_handler):
    """Test handling of a KeyError when executing a command."""
    with patch("builtins.input", side_effect=["1"]), patch.object(
        command_handler, "execute_command", side_effect=KeyError
    ):
        menu_command.execute()
        captured = capsys.readouterr()
        assert "Selected command could not be executed." in captured.out

def test_unexpected_error_handling(menu_command, capsys, command_handler):
    """Test handling of unexpected errors during command execution."""
    with patch("builtins.input", side_effect=["1"]), patch.object(
        command_handler, "execute_command", side_effect=Exception("Unexpected error")
    ):
        menu_command.execute()
        captured = capsys.readouterr()
        assert "An unexpected error occurred. Please try again." in captured.out
