import pandas as pd # type: ignore
import os

class HistoryManager:
    """
    Manages the history of calculations, stored in a CSV file.

    Attributes:
        file_path (str): Path to the CSV file where history records are stored.
    """

    def __init__(self, file_path='history.csv'):
        """
        Initializes the HistoryManager with a specified file path for the history file.
        
        If the file does not exist, it is created with the required headers.

        Args:
            file_path (str): Path to the CSV file for storing calculation history.
        """
        self.file_path = file_path
        # Initialize the CSV file with headers if it doesn't exist
        if not os.path.exists(self.file_path):
            self.clear_history()  

    def add_record(self, operation, num1, num2, result):
        """
        Adds a new record to the calculation history, maintaining only the last 5 records.

        Args:
            operation (str): The operation performed (e.g., "Add", "Multiply").
            num1 (float): The first number in the calculation.
            num2 (float): The second number in the calculation.
            result (float): The result of the calculation.
        """
        df = self.load_history()
        new_record = pd.DataFrame([{
            'Operation': operation,
            'Num1': num1,
            'Num2': num2,
            'Result': result
        }])
        
        # Ensure non-empty DataFrames to prevent warnings in future Pandas versions
        if not df.empty:
            df = pd.concat([df, new_record], ignore_index=True).tail(5)
        else:
            df = new_record  # Initialize df if empty

        df.to_csv(self.file_path, index=False)

    def load_history(self):
        """
        Loads calculation history from the CSV file.

        Returns:
            DataFrame: A DataFrame containing the calculation history records.
        """
        if os.path.exists(self.file_path):
            return pd.read_csv(self.file_path)
        # Return an empty DataFrame with specified columns if file doesn't exist
        return pd.DataFrame(columns=['Operation', 'Num1', 'Num2', 'Result'])

    def show_history(self):
        """
        Displays the history of calculations.

        Prints the contents of the history file if it exists; otherwise, 
        it displays a message indicating no history is available.
        """
        df = self.load_history()
        if df.empty:
            print("No history available.")
        else:
            print("Calculation History:\n", df)

    def clear_history(self):
        """
        Clears all records from the calculation history.

        Overwrites the history file with an empty DataFrame containing only headers.
        """
        pd.DataFrame(columns=['Operation', 'Num1', 'Num2', 'Result']).to_csv(self.file_path, index=False)
        print("History cleared.")

    def delete_record(self, index):
        """
        Deletes a specific record from the history by index.

        Args:
            index (int): The index of the record to delete.

        Prints a confirmation if the record is deleted or an error message if the index is invalid.
        """
        df = self.load_history()
        if 0 <= index < len(df):
            df = df.drop(index).reset_index(drop=True)
            df.to_csv(self.file_path, index=False)
            print(f"Record {index} deleted.")
        else:
            print("Invalid record index.")
