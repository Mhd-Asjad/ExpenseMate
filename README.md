# Expense Tracker CLI

A simple **command-line expense tracker** built with Python, Typer, and SQLAlchemy.  
It helps you manage expenses, categories, and budgets directly from your terminal.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Setup Expense (Add, view)
- Manage Categories (list)
- Add Budget Monthly Wise (Add, Update)
- Show Expense (category wise, monthly wise)
- Simple SQLite database with SQLAlchemy
- Lightweight CLI powered by click
- Editable install for development
---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Mhd-Asjad/ExpenseMate.git
    cd expense-tracker
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Linux/Mac
    venv\Scripts\activate      # On Windows
    ```

3. install in editable mode
    ```bash
    pip install -e .
    ```
## Usage

**run the CLI tool**

```bash
expense --help
```
*Example:*

```bash
cli commands

# Add an expense
expense add-expense "Lunch" 250 --category food

# Show expenses by category
expense show-category food

# Add Montly Budget
expense add-budget --month "2025-08" --amount 500

expensse show-expense "2025-08"

```

## project structure

```
expense_tracker/
│
├── expense_tracker/
│   ├── cli/              # CLI entry points (Typer commands)
│   │   └── cli.py
│   ├── database/         # Database setup and connection
│   │   └── db.py
│   ├── models/           # SQLAlchemy models
│   │   └── expense.py
│   ├── repositories/     # Data access layer
│   │   └── expense_repo.py
│   └── __init__.py
│
├── requirements.txt      # project Packages
├── pyproject.toml        # (optional) Modern build config
├── README.md             # Project documentation

```