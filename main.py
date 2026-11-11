"""Command-line Personal Expense Tracker."""
from datetime import datetime
from expense_tracker import ExpenseTracker

DATE_FORMAT = "%Y-%m-%d"

def ask_amount():
    while True:
        raw = input("Amount (€): ").strip()
        try:
            amount = float(raw)
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print("Please enter a valid amount greater than zero.")

def add_expense(tracker):
    print("\n--- Add Expense ---")
    title = input("Description: ").strip()
    while not title:
        print("Description cannot be empty.")
        title = input("Description: ").strip()

    amount = ask_amount()
    categories = ["Food", "Transport", "Shopping", "Education", "Housing", "Health", "Entertainment", "Other"]
    print("Categories:", ", ".join(categories))
    category = input("Category: ").strip().title()
    if category not in categories:
        category = "Other"

    date_text = input(f"Date [{datetime.today().strftime(DATE_FORMAT)}]: ").strip()
    if not date_text:
        date_text = datetime.today().strftime(DATE_FORMAT)
    try:
        datetime.strptime(date_text, DATE_FORMAT)
    except ValueError:
        print("Invalid date. Using today's date.")
        date_text = datetime.today().strftime(DATE_FORMAT)

    tracker.add_expense(title, amount, category, date_text)
    print("Expense saved successfully!")

def show_menu():
    print("""
========== PERSONAL EXPENSE TRACKER ==========
1. Add expense
2. View all expenses
3. Show summary
4. Category report
5. Delete expense
6. Exit
===============================================
""")

def main():
    tracker = ExpenseTracker()
    print("Welcome to Personal Expense Tracker!")
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_expense(tracker)
        elif choice == "2":
            tracker.display_expenses()
        elif choice == "3":
            tracker.display_summary()
        elif choice == "4":
            tracker.display_category_report()
        elif choice == "5":
            tracker.display_expenses()
            raw_id = input("Enter expense ID to delete: ").strip()
            if raw_id.isdigit() and tracker.delete_expense(int(raw_id)):
                print("Expense deleted.")
            else:
                print("Expense ID not found.")
        elif choice == "6":
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 6.")

if __name__ == "__main__":
    main()
