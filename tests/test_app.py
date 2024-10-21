"""
Unit tests for the App class, focusing on REPL commands and environment variable handling.
"""

import pytest
from app import App


def test_app_start_invalid_command_name(capfd, monkeypatch):
    """Test how the REPL handles an unknown string command before exiting."""
    # Simulate user entering an unknown string command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()

    # Verify the app exits with a valid SystemExit
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 0  # Can assert specific exit code if needed

    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()

    # Log the captured output for debugging
    print("Captured Output:\n", captured.out)

    # Only assert the relevant part of the output
    assert "Only numbers are allowed, wrong input." in captured.out, \
        f"Unexpected output: {captured.out}"


def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly when the 'exit' command is entered."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()

    # Expecting SystemExit when the 'exit' command is used
    with pytest.raises(SystemExit) as e:
        app.start()

    # Ensure the exception is indeed a SystemExit and check exit code if needed
    assert e.type == SystemExit
    assert e.value.code == 0  # Optional, but ensures a clean exit

    # Capture output and check if 'exit' command was executed properly
    captured = capfd.readouterr()
    print("Captured Output:\n", captured.out)


def test_app_get_environment_variable(monkeypatch):
    """Test retrieving environment variables from the App class."""
    app = App()

    # Monkeypatch the settings dictionary directly
    app.settings['ENVIRONMENT'] = 'TESTING'

    # Retrieve the environment setting
    current_env = app.get_environment_variable('ENVIRONMENT')

    # Assert that the current environment is as expected
    assert current_env == 'TESTING', f"Unexpected ENVIRONMENT: {current_env}"


def test_app_greet_command(capfd: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch):
    """Test that the REPL correctly handles the 'greet' command."""

    # Reusable input simulation for tests
    simulate_inputs(monkeypatch, ['3', 'exit'])

    app = App()

    # We expect a SystemExit when the 'exit' command is executed
    with pytest.raises(SystemExit) as excinfo:
        app.start()

    # Capture the output
    captured = capfd.readouterr()

    # Check that the 'greet' command prints "Hello, World!"
    assert "Hello, World!" in captured.out, "Greet command did not output as expected."

    # Ensure the application exits cleanly with exit code 0
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 0


def simulate_inputs(monkeypatch, inputs_list):
    """Helper function to simulate user input in REPL."""
    inputs = iter(inputs_list)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

# Add a final newline to avoid pylint error
