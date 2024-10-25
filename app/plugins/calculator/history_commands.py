# history_commands.py (in calculator plugin)

from app.commands import Command
from app.history_manager import HistoryManager
import logging

class ShowHistory(Command):
    def __init__(self):
        self.history_manager = HistoryManager()

    def execute(self):
        print("\nCalculation History:")
        self.history_manager.show_history()

class ClearHistory(Command):
    def __init__(self):
        self.history_manager = HistoryManager()

    def execute(self):
        self.history_manager.clear_history()
        print("History has been cleared.")

class DeleteSpecificRecord(Command):
    def __init__(self):
        self.history_manager = HistoryManager()

    def execute(self):
        try:
            index = int(input("Enter the record index to delete: "))
            self.history_manager.delete_record(index)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
