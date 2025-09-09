
# Expense Tracker

A Python-based expense tracking application to help you manage and analyze your daily expenses efficiently.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [File Overview](#file-overview)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add, edit, and delete expense records
- Categorize expenses
- View expense history and summary statistics
- Export data to CSV
- Simple command-line interface

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/expense_tracker.git
    ```
2. Install dependencies (if any):
    ```bash
    cd expense_tracker
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python main.py
    ```

## Usage

- Launch the app and follow the prompts to add, view, edit, or delete expenses.
- Use filtering options to view expenses by category or date.
- Export your expense data for further analysis.

## Project Structure

```
expense_tracker/
├── cli.py              # Entry point for the application
├── database.py           # Expense model and logic
├── tracker.py           # Core tracking functionality
├── utils.py             # Utility functions (e.g., CSV export)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## File Overview

- **main.py**: Handles user interaction and command-line interface.
- **expense.py**: Defines the Expense class and related methods for managing expense data.
- **tracker.py**: Implements the logic for adding, editing, deleting, and summarizing expenses.
- **utils.py**: Contains helper functions, such as exporting expenses to CSV.
- **requirements.txt**: Lists required Python packages (e.g., pandas, tabulate).

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License.
