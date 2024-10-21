import pandas as pd

class CalculationHistory:
    def __init__(self, file_name='calculation_history.csv'):
        self.file_name = file_name
        self.history = pd.DataFrame(columns=["Operation", "Input1", "Input2", "Result"])
    
    def add_to_history(self, operation, input1, input2, result):
        # Add the new calculation to the history DataFrame
        new_entry = {"Operation": operation, "Input1": input1, "Input2": input2, "Result": result}
        self.history = pd.concat([self.history, pd.DataFrame([new_entry])], ignore_index=True)
        
        # Save history to CSV, limiting the entries to the last 5 calculations
        if len(self.history) > 5:
            self.history = self.history.iloc[-5:]
        self.history.to_csv(self.file_name, index=False)

    def show_history(self):
        # Read from the CSV file and display the history
        try:
            self.history = pd.read_csv(self.file_name)
        except FileNotFoundError:
            print("No history found. Start calculating!")
        print(self.history)


