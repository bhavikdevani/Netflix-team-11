"""Core logic for storing and reporting expenses."""
import csv
import os
from collections import defaultdict

class ExpenseTracker:
    HEADERS = ["id", "date", "description", "category", "amount"]

    def __init__(self, filename="data/expenses.csv"):
        self.filename = filename
        self.expenses = []
        self._next_id = 1
        self._load_expenses()

    def _load_expenses(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    expense = {
                        "id": int(row["id"]),
                        "date": row["date"],
                        "description": row["description"],
                        "category": row["category"],
                        "amount": float(row["amount"]),
                    }
                    self.expenses.append(expense)
                except (KeyError, TypeError, ValueError):
                    # Ignore malformed rows instead of stopping the application.
                    continue
        if self.expenses:
            self._next_id = max(item["id"] for item in self.expenses) + 1

    def _save_expenses(self):
        folder = os.path.dirname(self.filename)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.HEADERS)
            writer.writeheader()
            writer.writerows(self.expenses)

    def add_expense(self, description, amount, category, date):
        description = str(description).strip()
        category = str(category).strip().title()
        if not description:
            raise ValueError("Description cannot be empty.")
        if not category:
            raise ValueError("Category cannot be empty.")
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if not isinstance(date, str) or len(date) != 10:
            raise ValueError("Date must use YYYY-MM-DD format.")

        expense = {
            "id": self._next_id,
            "date": date,
            "description": description,
            "category": category,
            "amount": round(amount, 2),
        }
        self.expenses.append(expense)
        self._next_id += 1
        self._save_expenses()
        return expense

    def delete_expense(self, expense_id):
        original_count = len(self.expenses)
        self.expenses = [e for e in self.expenses if e["id"] != expense_id]
        if len(self.expenses) == original_count:
            return False
        self._save_expenses()
        return True

    def total_expenses(self):
        return round(sum(e["amount"] for e in self.expenses), 2)

    def category_totals(self):
        totals = defaultdict(float)
        for expense in self.expenses:
            totals[expense["category"]] += expense["amount"]
        return {key: round(value, 2) for key, value in sorted(totals.items())}

    def display_expenses(self):
        if not self.expenses:
            print("\nNo expenses found.")
            return
        print("\nID | Date       | Description          | Category       | Amount")
        print("-" * 75)
        for e in self.expenses:
            print(f'{e["id"]:<2} | {e["date"]:<10} | {e["description"][:20]:<20} | '
                  f'{e["category"][:14]:<14} | €{e["amount"]:>8.2f}')

    def display_summary(self):
        print(f"\nNumber of expenses: {len(self.expenses)}")
        print(f"Total spent: €{self.total_expenses():.2f}")

    def display_category_report(self):
        totals = self.category_totals()
        if not totals:
            print("\nNo category data available.")
            return
        print("\n--- Category Report ---")
        for category, amount in totals.items():
            print(f"{category:<18} €{amount:.2f}")
