from app.commands import Command
from app.history_manager import HistoryManager
import logging

class ShowHistory(Command):
    """
    Command to display the calculation history.
    
    Attributes:
        history_manager (HistoryManager): Manages the history of calculation records.
    """

    def __init__(self):
        """
        Initializes the ShowHistory command with a history manager to retrieve calculation history.
        """
        self.history_manager = HistoryManager()

    def execute(self):
        """
        Executes the show history command, displaying all records in the calculation history.
        """
        print("\nCalculation History:")
        self.history_manager.show_history()


class ClearHistory(Command):
    """
    Command to clear all records from the calculation history.
    
    Attributes:
        history_manager (HistoryManager): Manages the history of calculation records.
    """

    def __init__(self):
        """
        Initializes the ClearHistory command with a history manager to clear all calculation records.
        """
        self.history_manager = HistoryManager()

    def execute(self):
        """
        Executes the clear history command, removing all records from the calculation history 
        and confirming the action to the user.
        """
        self.history_manager.clear_history()
        print("History has been cleared.")


class DeleteSpecificRecord(Command):
    """
    Command to delete a specific record from the calculation history by index.
    
    Attributes:
        history_manager (HistoryManager): Manages the history of calculation records.
    """

    def __init__(self):
        """
        Initializes the DeleteSpecificRecord command with a history manager to delete individual records.
        """
        self.history_manager = HistoryManager()

    def execute(self):
        """
        Executes the delete specific record command, prompting the user to specify a record index 
        to delete from the calculation history.

        Handles invalid input with an error message.
        
        Raises:
            ValueError: If the input is not a valid integer.
        """
        try:
            index = int(input("Enter the record index to delete: "))
            self.history_manager.delete_record(index)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
