# Expense Tracker

A simple command-line Expense Tracker built with Python. The application allows users to record expenses, view saved transactions, calculate spending by category, and monitor their total spending.

## Features

- Add new expenses with a date, category, description, and amount.
- View all recorded expenses in a formatted table.
- Calculate total spending for each category.
- Calculate overall spending.
- Store expense records permanently using CSV files.
- Handle invalid inputs and file-related errors gracefully.

## Project Structure

```text
expense-tracker/
├── main.py
├── expenses.csv
├── README.md
└── screenshots/
```

## Technologies Used

- Python
- CSV module
- pathlib
- Exception handling
- Dictionaries and lists

## Error Handling

The application handles:

- Missing CSV files by creating a new file.
- Empty CSV files without crashing.
- Invalid expense amounts.
- Zero and negative expense amounts.
- Invalid menu selections.
- CSV records containing invalid amounts.
- File permission and operating system errors.

## Data Storage
Expense records are stored in `expenses.csv` using the following columns:

- Date
- Category
- Description
- Amount

## This is my demo video 