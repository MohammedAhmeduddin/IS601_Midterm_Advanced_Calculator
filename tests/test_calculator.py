"""
Unit tests for the Calculator plugin commands.
"""

import unittest
from unittest.mock import patch
from app.plugins.calculator.add import Add
from app.plugins.calculator.subtract import Subtract
from app.plugins.calculator.multiply import Multiply
from app.plugins.calculator.divide import Divide


class TestCalculatorCommands(unittest.TestCase):
    """
    Tests for calculator command functionalities.

    This class contains unit tests for each arithmetic command, verifying that the commands
    correctly execute addition, subtraction, multiplication, and division operations.
    """

    @patch('builtins.input', side_effect=[5, 3])
    @patch('builtins.print')
    def test_add(self, mock_print, mock_input):
        """
        Test addition operation.

        Mocks user input for two numbers, executes the Add command, and verifies that the output
        is as expected.
        """
        # Instantiate the Add command
        add_command = Add()
        # Execute the command
        add_command.execute()
        # Check that the print statement was called with the correct output
        mock_print.assert_called_with("The result of 5.0 + 3.0 is 8.0")

    @patch('builtins.input', side_effect=[5, 3])
    @patch('builtins.print')
    def test_subtract(self, mock_print, mock_input):
        """
        Test subtraction operation.

        Mocks user input for two numbers, executes the Subtract command, and verifies that the output
        is as expected.
        """
        # Instantiate the Subtract command
        subtract_command = Subtract()
        # Execute the command
        subtract_command.execute()
        # Check that the print statement was called with the correct output
        mock_print.assert_called_with("The result of 5.0 - 3.0 is 2.0")

    @patch('builtins.input', side_effect=[5, 3])
    @patch('builtins.print')
    def test_multiply(self, mock_print, mock_input):
        """
        Test multiplication operation.

        Mocks user input for two numbers, executes the Multiply command, and verifies that the output
        is as expected.
        """
        # Instantiate the Multiply command
        multiply_command = Multiply()
        # Execute the command
        multiply_command.execute()
        # Check that the print statement was called with the correct output
        mock_print.assert_called_with("The result of 5.0 * 3.0 is 15.0")

    @patch('builtins.input', side_effect=[6, 3])
    @patch('builtins.print')
    def test_divide(self, mock_print, mock_input):
        """
        Test division operation.

        Mocks user input for two numbers, executes the Divide command, and verifies that the output
        is as expected.
        """
        # Instantiate the Divide command
        divide_command = Divide()
        # Execute the command
        divide_command.execute()
        # Check that the print statement was called with the correct output
        mock_print.assert_called_with("The result of 6.0 / 3.0 is 2.0")

if __name__ == '__main__':
    unittest.main()
