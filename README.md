# Personal Expense Tracker (Python)

A beginner-friendly command-line application to record personal expenses, save them in a CSV file, and review spending summaries.

## Features

- Add expenses with a description, amount, category, and date
- View all saved expenses
- Calculate total spending
- View spending grouped by category
- Delete an expense by its ID
- Store data locally in `data/expenses.csv`
- Validate input and handle invalid menu choices
- Unit tests using Python's built-in `unittest` module

## Technologies

- Python 3.9+
- CSV (built-in Python module)
- `unittest` (built-in Python testing framework)

No third-party packages are required.

## Project structure

```text
personal-expense-tracker/
├── data/
│   └── .gitkeep
├── tests/
│   └── test_expense_tracker.py
├── .gitignore
├── README.md
├── expense_tracker.py
├── main.py

```

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/personal-expense-tracker.git
cd personal-expense-tracker
```

### 2. Run the application

Make sure Python 3 is installed, then run:

```bash
python main.py
```

On some systems, use `python3 main.py`.

### 3. Use the menu

Choose an option:
1. Add expense
2. View all expenses
3. Show summary
4. Category report
5. Delete expense
6. Exit

Your expense data is saved automatically to `data/expenses.csv`.

## Run the tests

From the project root, run:

```bash
python -m unittest discover -s tests -v
```

## Example

```text
Welcome to Personal Expense Tracker!

1. Add expense
2. View all expenses
3. Show summary
4. Category report
5. Delete expense
6. Exit
```

## Data and privacy

The application stores expenses locally in a CSV file. Do not commit personal financial records to a public GitHub repository. The `.gitignore` file excludes the generated CSV file.

## Possible improvements

- Monthly budget limits and warnings
- Export reports to Excel
- Visual charts with Matplotlib
- A graphical interface using Tkinter
- Search and filter expenses by date or category


