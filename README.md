
# IS601 Midterm Advanced Calculator

## Overview

This project is a modular and extensible Python-based command-line calculator application. It supports various arithmetic operations and history management, leveraging a flexible plugin-based architecture. The project is structured with maintainability, scalability, and clear separation of concerns in mind, following best coding practices and incorporating several design patterns.

## Features

- **Arithmetic Operations**: Perform addition, subtraction, multiplication, and division.
- **History Management**: Save, load, and manage calculation history using CSV files and `pandas`.
- **Command Pattern**: Executes commands in a consistent manner using a `Command` and `CommandHandler` setup.
- **Logging**: Comprehensive logging configuration tracks command registration, execution, and errors.
- **Plugin-based Architecture**: Supports modular commands such as `greet`, `calculator`, `menu`, and `exit`, allowing easy expansion of functionality.
- **CI/CD Integration**: GitHub Actions workflow for automated testing and deployment.

## Design Patterns Implemented

### 1. Command Pattern

The **Command Pattern** encapsulates each command as an object, allowing flexible handling of operations. By using this pattern, we can implement commands like `add`, `subtract`, `multiply`, and `divide` as individual classes, making the command execution modular and extensible.

- **Why this pattern?** The Command Pattern was chosen for its flexibility in adding new operations without altering existing code. Each arithmetic operation is treated as a command, enabling encapsulated execution and consistency.

- **Implementation Links**:
  - [Addition Command](app/plugins/calculator/add.py)
  - [Subtraction Command](app/plugins/calculator/subtract.py)
  - [History Commands](app/plugins/calculator/history_commands.py)
  
### 2. Facade Pattern

The **Facade Pattern** is used in `history_manager.py` to simplify complex operations related to history management, including saving, loading, clearing, and deleting records.

- **Why this pattern?** This pattern abstracts the internal details of history management, making it easier for the client (main application) to interact with the history system. It reduces the need for the main application to know about data handling specifics, streamlining the process of managing history.

- **Implementation Link**:
  - [History Manager (Facade)](app/history_manager.py)
  
### 3. Singleton Pattern

The **Singleton Pattern** ensures that configuration settings (e.g., logging configurations) exist only once within the application.

- **Why this pattern?** By using Singleton, we prevent multiple instances of the same configuration, which helps maintain consistency and saves resources.

- **Implementation Link**:
  - [Logging Configuration](logging.conf)

### 4. Plugin Architecture

The **Plugin Architecture** is fundamental to the application’s extensibility. Each plugin, such as `greet`, `calculator`, `menu`, and `exit`, is designed to be self-contained, which allows easy addition and customization of commands.

- **Why this pattern?** This architecture is ideal for applications that need dynamic functionality. By structuring commands as plugins, we allow users to add, remove, or modify commands without impacting the core system.

- **Implementation Links**:
  - [Calculator Plugins](app/plugins/calculator/)
  - [Greet Plugin](app/plugins/greet/__init__.py)
  - [Menu Plugin](app/plugins/menu/__init__.py)
  - [Exit Plugin](app/plugins/exit/__init__.py)



## Usage

Run the main application from the command line:

```bash
python main.py
```

### Commands

Each command corresponds to a specific functionality, accessible in the REPL interface:

- **Calculator Operations**: 
  - `add <number1> <number2>`: Adds two numbers.
  - `subtract <number1> <number2>`: Subtracts second number from the first.
  - `multiply <number1> <number2>`: Multiplies two numbers.
  - `divide <number1> <number2>`: Divides the first number by the second.
  
- **History Commands**: Manage past calculations:
  - `save`: Save the current calculations to history.
  - `load`: Load and display calculation history.
  - `clear`: Clear all history records.
  - `delete <record_id>`: Deletes a specific record from history.

- **Other Commands**: 
  - `greet`: Greets the user.
  - `menu`: Shows available commands.
  - `exit`: Closes the application.

## Testing

The project includes a comprehensive test suite located in the `tests` folder. Each component has corresponding tests to ensure reliability and robustness. Run tests with `pytest`:

```bash
pytest
```

## CI/CD Pipeline

The project uses GitHub Actions for CI/CD, which automates testing and ensures code integrity. Every push or pull request triggers automated tests, ensuring consistent application behavior and minimizing risk in the development process.

## Logging Configuration

Logging is set up in `logging.conf` with configurations for different levels of logging (e.g., INFO, DEBUG, ERROR). Key logged actions include:

- **Command Execution**: Logs each command executed, capturing user input and any results.
- **Error Handling**: Captures errors in the application, facilitating debugging.
- **History Management**: Logs actions related to saving, loading, and clearing history.

## Dependencies

Dependencies for the project are listed in `requirements.txt`, including:

- `pandas`: For managing calculation history data.
- `pytest`: For running tests.

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Video Link:

