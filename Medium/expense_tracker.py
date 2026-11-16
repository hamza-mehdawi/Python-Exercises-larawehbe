"""Expense Tracker CLI """
import os
import pandas as pd
from datetime import date

FILE = "expenses.csv"


class Expense:
    def __init__(self, category, amount, date):
        self.category, self.amount, self.date = category, float(amount), date


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount, date):
        self.expenses.append(Expense(category, amount, date))

    def view_expenses(self):
        if not self.expenses:
            print("No expenses yet.")
        for i, e in enumerate(self.expenses, 1):
            print(f"{i}. {e.date} | {e.category} | {e.amount:.2f}")

    def category_summary(self):
        totals = {}
        for e in self.expenses:
            totals[e.category] = totals.get(e.category, 0) + e.amount
        for cat, total in totals.items():
            print(f"{cat}: {total:.2f}")
        return totals

    def save_to_csv(self, path=FILE):
        pd.DataFrame([vars(e) for e in self.expenses]).to_csv(path, index=False)
        print(f"Saved {len(self.expenses)} expenses to {path}")

    def load_from_csv(self, path=FILE):
        if not os.path.exists(path):
            print("No saved file found.")
            return
        df = pd.read_csv(path)
        self.expenses = [Expense(r.category, r.amount, r.date) for r in df.itertuples()]
        print(f"Loaded {len(self.expenses)} expenses from {path}")


def main():
    m = ExpenseManager()
    while True:
        c = input("\n1) Add  2) View  3) Summary  4) Save  5) Load  6) Exit\nChoice: ").strip()
        if c == "1":
            cat = input("Category: ").strip()
            try:
                amt = float(input("Amount: "))
            except ValueError:
                print("Amount must be a number.")
                continue
            d = input("Date (YYYY-MM-DD, empty = today): ").strip() or str(date.today())
            m.add_expense(cat, amt, d)
        elif c == "2":
            m.view_expenses()
        elif c == "3":
            m.category_summary()
        elif c == "4":
            m.save_to_csv()
        elif c == "5":
            m.load_from_csv()
        elif c == "6":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
