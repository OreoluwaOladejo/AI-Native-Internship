import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
#This will get the folder containing this file.(Which is the main.py)
#It will bring out something like this 
#"C:\Users\oreol\OneDrive\Desktop\Python API\Flexisaf\Week 6"



FILE_PATH = BASE_DIR / "expenses.csv"

#This will give 
# "C:\Users\oreol\OneDrive\Desktop\Python API\Flexisaf\Week 6\expense_tracker\expenses.csv"

#We have to load the expenses from the CSV FILE
def load_expenses():
    expenses = []
    try:
        # Open the CSV file in read mode.
        with open(FILE_PATH, mode="r", newline="") as file:

            # DictReader reads each CSV row into a dictionary.
            reader = csv.DictReader(file)

            # If the CSV is completely empty, return an empty list.
            if reader.fieldnames is None:
                return expenses

            # Read each row in the CSV file.
            for row in reader:
                try:
                    # Convert the amount from a string to a float.
                    row["amount"] = float(row["amount"])

                    # Add the valid expense to our list.
                    expenses.append(row)

                except (ValueError, TypeError):
                    # Skip rows with invalid or missing amounts.
                    print("Warning: A record with an invalid amount was skipped.")

    except FileNotFoundError:

        # If the file does not exist, create it with the required headers.
        with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=["date", "category", "description", "amount"]
            )

            writer.writeheader()

        print("Expense file created successfully.")
    except (PermissionError, OSError):
        print("Unable to access the expense file.")

    return expenses

#We are creating the funcion for adding expenses 
def add_expense(expenses):
    print("\n ADD NEW EXPENSE")

    # Collect the expense details.
    date = input("Enter date (YYYY-MM-DD):").strip()

    category = input("Enter the category: ").strip()

    description = input("Enter description: ").strip()

    #For amount we have to validate it 
    while True:
        try:
            amount = float(input("Enter amount: ").strip())

            # Reject zero and negative amounts.
            if amount <= 0:
                print("Amount must be greater than zero. Try again.")
                continue
            else:
              break

        except ValueError:
            print("Please enter a valid number.")

    # Create a dictionary for the new expense.
    new_expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    try:
        # Append the new expense to the CSV file.
        with open(FILE_PATH, mode="a", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=["date", "category", "description", "amount"]
            )

            writer.writerow(new_expense)

        # Update the in-memory list only after a successful write.
        expenses.append(new_expense)

        print("\nExpense added successfully")

    except PermissionError:
        print("Permission denied. Please check that the file is not locked.")

    except OSError:
        print("Unable to save the expense. Please try again.")

#We are creating the function for reading or getting all expenses 
def view_expenses(expenses):
    print("\n ALL EXPENSES ")

    # Check whether there are any expenses to display.
    if not expenses:
        print("No expenses recorded yet.")
        return

    # Print the table headings.
    print("-" * 85)

    print(
        f"{'DATE':<15}"
        f"{'CATEGORY':<18}"
        f"{'DESCRIPTION':<30}"
        f"{'AMOUNT':>15}"
    )

    print("-" * 85)

    # Display each expense.
    for expense in expenses:

        print(
            f"{expense['date']:<15}"
            f"{expense['category']:<18}"
            f"{expense['description']:<30}"
            f"{expense['amount']:>15,.2f}"
        )

    print("-" * 85)

#This is to calculate and display the total spending for each category
def summary_by_category(expenses):
    print("\nSUMMARY BY CATEGORY ")

    # Check whether there are any expenses.
    if not expenses:
        print("No expenses available for summary.")
        return

    # Create an empty dictionary to store category totals.
    totals = {}

    # Loop through every expense.
    for expense in expenses:

        category = expense["category"]

        amount = expense["amount"]

        # If the category does not exist, initialize it to zero.
        if category not in totals:
            totals[category] = 0

        # Add the expense amount to the category total.
        totals[category] += amount

    # Display the calculated totals.
    print("-" * 40)

    for category, total in totals.items():
        print(f"{category:<20} ₦{total:,.2f}")

    print("-" * 40)

#This is to calculate and display the total amount spent across all categories.
def total_spending(expenses):
    print("\n TOTAL SPENDING ")

    # Calculate the sum of all expense amounts.
    total = sum(i["amount"] for i in expenses)

    print(f"Your total spending is: ₦{total:,.2f}")

#This si teh main function that callss of the function and shows the menu continuously
def main():
    # Load existing expenses when the application starts.
    expenses = load_expenses()
    print("\n WELCOME TO EXPENSE TRACKER")

    # Keep the application running until the user exits.
    while True:

        print("\n MAIN MENU ")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Summary by category")
        print("4. Total spending")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            summary_by_category(expenses)

        elif choice == "4":
            total_spending(expenses)

        elif choice == "5":
            print("\nThank you for using Expense Tracker")
            print("Bye bye!")
            break

        else:
            print("\nInvalid choice. Please select a number between 1 and 5.")


# This ensures main() runs when we execute this file directly.
if __name__ == "__main__":
    main()