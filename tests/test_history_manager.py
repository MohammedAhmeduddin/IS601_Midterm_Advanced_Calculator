"""
Test suite for HistoryManager class, which handles loading, saving, and
managing a calculation history in a CSV file.
"""

import os
import pytest
import pandas as pd # type: ignore
from app.history_manager import HistoryManager

@pytest.fixture
def history_manager(tmp_path):
    """Fixture to initialize HistoryManager with a temporary file path."""
    file_path = tmp_path / "test_history.csv"
    return HistoryManager(file_path=str(file_path))

def test_file_initialization(history_manager):
    """Test that the file is initialized with headers if it doesn't exist."""
    assert os.path.exists(history_manager.file_path)
    df = pd.read_csv(history_manager.file_path)
    assert list(df.columns) == ['Operation', 'Num1', 'Num2', 'Result']

def test_add_record(history_manager):
    """Test adding a record to history."""
    history_manager.add_record('add', 1, 2, 3)
    df = pd.read_csv(history_manager.file_path)
    assert len(df) == 1
    assert df.iloc[0].to_dict() == {'Operation': 'add', 'Num1': 1, 'Num2': 2, 'Result': 3}

def test_load_history(history_manager):
    """Test loading history from file."""
    history_manager.add_record('subtract', 5, 3, 2)
    df = history_manager.load_history()
    assert len(df) == 1
    assert df.iloc[0].to_dict() == {'Operation': 'subtract', 'Num1': 5, 'Num2': 3, 'Result': 2}

def test_clear_history(history_manager):
    """Test clearing history."""
    history_manager.add_record('multiply', 2, 3, 6)
    history_manager.clear_history()
    df = history_manager.load_history()
    assert df.empty

def test_limit_history_to_last_5_records(history_manager):
    """Test that only the last 5 records are kept in the history."""
    for i in range(7):
        history_manager.add_record('add', i, i + 1, i + 2)
    df = history_manager.load_history()
    assert len(df) == 5  # Only the last 5 records should remain
    assert df.iloc[0].to_dict() == {'Operation': 'add', 'Num1': 2, 'Num2': 3, 'Result': 4}

def test_delete_record(history_manager):
    """Test deleting a specific record by index."""
    for i in range(3):
        history_manager.add_record('subtract', i + 2, i, i + 2)
    history_manager.delete_record(1)  # Delete the second record
    df = history_manager.load_history()
    assert len(df) == 2  # One record should be deleted
    assert df.iloc[0].to_dict() == {'Operation': 'subtract', 'Num1': 2, 'Num2': 0, 'Result': 2}
    assert df.iloc[1].to_dict() == {'Operation': 'subtract', 'Num1': 4, 'Num2': 2, 'Result': 4}

def test_delete_invalid_record(history_manager, capsys):
    """Test deleting an invalid record index."""
    history_manager.add_record('divide', 10, 2, 5)
    history_manager.delete_record(5)  # Invalid index
    captured = capsys.readouterr()
    assert "Invalid record index." in captured.out
