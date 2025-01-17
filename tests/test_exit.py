"""
Unit tests for the ExitCommand in the exit plugin.
"""

import unittest
from unittest.mock import patch
from app.plugins.exit import ExitCommand


class TestExitCommand(unittest.TestCase):
    """
    Tests for the ExitCommand class.

    This class tests the behavior of the execute method in ExitCommand, ensuring 
    it logs the appropriate messages and exits the application with the correct message.
    """

    @patch('builtins.print')
    @patch('app.plugins.exit.logging.info')  # Mock logging
    def test_execute_exit(self, mock_logging, mock_print):
        """
        Test the execute method of ExitCommand.

        Verifies that the command logs the exit message, triggers a SystemExit, and that
        the SystemExit exception message matches the expected "Exiting...".
        """
        exit_command = ExitCommand()

        with self.assertRaises(SystemExit) as cm:
            exit_command.execute()

        # Check that the exit message is as expected
        self.assertEqual(str(cm.exception), "Exiting...")

        # Check that the logging was called correctly
        mock_logging.assert_any_call("ExitCommand executed: Application is exiting.")
        mock_logging.assert_any_call("System exit with message: Exiting...")


if __name__ == '__main__':
    unittest.main()
