"""
Unit tests for the GreetCommand in the greet plugin.
"""

import unittest
from unittest.mock import patch
from app.plugins.greet import GreetCommand


class TestGreetCommand(unittest.TestCase):
    """
    Tests for the GreetCommand class.

    This class tests the execute method in GreetCommand to ensure it outputs
    the expected greeting message.
    """

    @patch('builtins.print')
    def test_execute_greet(self, mock_print):
        """
        Test the execute method of GreetCommand.

        Verifies that executing the greet command outputs "Hello, World!" by
        checking the call to the print function.
        """
        # Instantiate the GreetCommand
        greet_command = GreetCommand()
        # Execute the command
        greet_command.execute()
        # Check that the print statement was called with the correct output
        mock_print.assert_called_with("Hello, World!")


if __name__ == '__main__':
    unittest.main()
