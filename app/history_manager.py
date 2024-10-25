import pandas as pd
import os

class HistoryManager:
    def __init__(self, file_path='history.csv'):
        self.file_path = file_path
        # Initialize the CSV file with headers if it doesn't exist
        if not os.path.exists(self.file_path):
            self.clear_history()  

    def add_record(self, operation, num1, num2, result):
        """Add a new record to the calculation history, keeping only the last 5 records."""
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
        """Load calculation history from the CSV file."""
        if os.path.exists(self.file_path):
            return pd.read_csv(self.file_path)
        # Return an empty DataFrame with specified columns if file doesn't exist
        return pd.DataFrame(columns=['Operation', 'Num1', 'Num2', 'Result'])

    def show_history(self):
        """Display the history of calculations."""
        df = self.load_history()
        if df.empty:
            print("No history available.")
        else:
            print("Calculation History:\n", df)

    def clear_history(self):
        """Clear all records from the calculation history."""
        pd.DataFrame(columns=['Operation', 'Num1', 'Num2', 'Result']).to_csv(self.file_path, index=False)
        print("History cleared.")

    def delete_record(self, index):
        """Delete a specific record from the history by index."""
        df = self.load_history()
        if 0 <= index < len(df):
            df = df.drop(index).reset_index(drop=True)
            df.to_csv(self.file_path, index=False)
            print(f"Record {index} deleted.")
        else:
            print("Invalid record index.")
