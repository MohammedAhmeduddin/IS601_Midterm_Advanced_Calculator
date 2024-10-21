# main.py
from app import App    
from app.plugins.history.history_manager import CalculationHistory

def perform_calculation():
    history_manager = CalculationHistory()
    
    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Show history")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice in ['1', '2', '3', '4']:
            try:
                input1 = float(input("Enter first number: "))
                input2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = input1 + input2
                    operation = "Addition"
                elif choice == '2':
                    result = input1 - input2
                    operation = "Subtraction"
                elif choice == '3':
                    result = input1 * input2
                    operation = "Multiplication"
                elif choice == '4':
                    if input2 == 0:
                        print("Cannot divide by zero. Try again.")
                        continue
                    result = input1 / input2
                    operation = "Division"
                
                print(f"Result: {result}")
                
                # Add the calculation to history
                history_manager.add_to_history(operation, input1, input2, result)
            
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        
        elif choice == '5':
            # Show the calculation history
            history_manager.show_history()
        
        elif choice == '6':
            print("Exiting the calculator.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    perform_calculation()

# You must put this in your main.py because this forces the program to start when you run it from the command line.
if __name__ == "__main__":
    app = App().start()  # Instantiate an instance of App