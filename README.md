
# IS601 Midterm Advanced Calculator

## Introduction

This project presents a modular and extendable Python-based calculator for the command line, featuring core arithmetic functions and a robust history management system. Designed with modularity and extensibility in mind, it uses a plugin-based architecture that enables flexible customization. The code adheres to best practices for clean design, making use of multiple design patterns.

## Key Features

- **Arithmetic Functions**: Basic operations including addition, subtraction, multiplication, and division.
- **History Management**: Easily manage past calculations by saving, loading, and editing them with CSV and `pandas` support.
- **Command Pattern**: Each command is handled uniformly via a `Command` and `CommandHandler` system.
- **Comprehensive Logging**: Logs track command executions and errors for easy debugging.
- **Plugin-Based Flexibility**: Plugins like `greet`, `calculator`, `menu`, and `exit` allow seamless extension.
- **CI/CD with GitHub Actions**: Automated testing and continuous integration streamline code validation.

## Design Patterns and Rationale

### 1. Command Pattern

The **Command Pattern** enables each action (e.g., addition, subtraction) to be represented as an object. By encapsulating each operation as a command, we achieve a modular and consistent method for adding and handling operations.

- **Why use this pattern?** It enables easy addition of new operations with minimal impact on existing code, making the calculator highly flexible.
- **Code References**:
  - [Addition Command](app/plugins/calculator/add.py)
  - [Subtraction Command](app/plugins/calculator/subtract.py)
  - [History Commands](app/plugins/calculator/history_commands.py)

### 2. Facade Pattern

The **Facade Pattern** is implemented in `history_manager.py` to provide an easier interface for complex operations like saving, loading, and modifying calculation records.

- **Why use this pattern?** This pattern streamlines interactions with the history management system by hiding complex internal operations, enhancing code simplicity.
- **Code Reference**:
  - [History Manager as Facade](app/history_manager.py)

### 3. Singleton Pattern

The **Singleton Pattern** is applied to configurations, particularly for logging, to ensure only a single instance is present throughout the application.

- **Why use this pattern?** This prevents multiple configuration instances, ensuring consistency and efficient resource usage.
- **Code Reference**:
  - [Logging Configuration](logging.conf)

### 4. Plugin Architecture

The **Plugin Architecture** is the backbone of the calculator’s flexibility, enabling commands like `greet`, `calculator`, `menu`, and `exit` to be loaded dynamically and work independently.

- **Why use this pattern?** It provides dynamic functionality that is easily customizable, allowing new features to be added without modifying core components.
- **Code References**:
  - [Calculator Plugins](app/plugins/calculator/)
  - [Greet Plugin](app/plugins/greet/__init__.py)
  - [Menu Plugin](app/plugins/menu/__init__.py)
  - [Exit Plugin](app/plugins/exit/__init__.py)

## Environment Variables

Environment variables are used to store configuration details securely and dynamically, such as file paths for logging and history. This ensures that sensitive information or settings are not hardcoded. Configuration using environment variables allows easy adjustments without modifying the code itself.

- **Code Reference**:
  - [Environment Variable Setup in `main.py`](main.py)

## Logging Configuration

Logging is set up using a dedicated `logging.conf` file to capture various log levels, including INFO, DEBUG, and ERROR. Key actions logged include:

- **Command Executions**: Every command executed (e.g., `add`, `subtract`) is logged to capture user interactions.
- **Errors**: Errors are logged, providing a record of any exceptions that occur, which aids in debugging.
- **History Changes**: Actions like saving and clearing history are recorded, adding traceability to history management.

- **Code Reference**:
  - [Logging Configuration](logging.conf)

## Exception Handling: LBYL and EAFP Patterns

Exception handling is a crucial part of this project, using both **Look Before You Leap (LBYL)** and **Easier to Ask for Forgiveness than Permission (EAFP)** patterns to manage errors effectively:

- **LBYL**: For certain operations, the application checks if conditions are met before proceeding, which helps avoid exceptions proactively.
- **EAFP**: In scenarios where errors may unpredictably occur, the application catches exceptions directly to handle them gracefully.

- **Code References**:
  - [LBYL Example in `history_manager.py`](app/history_manager.py)
  - [EAFP Example in `main.py`](main.py)


## Instructions for Use

To start the application from the command line:

```bash
python main.py
```

### Available Commands

In the REPL interface, use the following commands:

- **Calculator Functions**: 
  - `add <number1> <number2>`: Adds two values.
  - `subtract <number1> <number2>`: Subtracts the second number from the first.
  - `multiply <number1> <number2>`: Multiplies two numbers.
  - `divide <number1> <number2>`: Divides the first number by the second.
  
- **History Management**:
  - `save`: Save current calculations.
  - `load`: Retrieve and view previous calculations.
  - `clear`: Remove all records from history.
  - `delete <record_id>`: Deletes a specific entry.

- **General Commands**:
  - `greet`: Display a greeting message.
  - `menu`: Lists all available commands.
  - `exit`: Terminates the application.

## Testing Suite

A full suite of tests is included in the `tests` directory. Each function is tested to ensure stability. Run tests with `pytest`:

```bash
pytest
```

## CI/CD Workflow

The project uses GitHub Actions to automate testing, ensuring code quality and integrity for each push or pull request.

## Video Link:


