"""Personal Expense Tracker

A simple command-line application to record and analyse daily expenses.
Expenses are stored in memory for the duration of the session.
"""

expenses = []


def add_expense():
    """Prompt the user for expense details and add them to the list."""
    print("Add Expense")

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    summary = input("Enter summary: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "summary": summary,
    }

    expenses.append(expense)
    print("Expense added successfully.")


def print_expense(expense):
    """Print the details of a single expense."""
    print("Date:", expense["date"])
    print("Category:", expense["category"])
    print("Amount: Rs.", expense["amount"])
    print("Summary:", expense["summary"])


def view_expenses():
    """Display all recorded expenses."""
    print("All Expenses")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for i in range(len(expenses)):
        print("Expense", i + 1)
        print_expense(expenses[i])


def total_expense():
    """Display the total of all expenses."""
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense: Rs.", total)


def category_expense():
    """Display the total spent in a category (case-insensitive)."""
    print("Category Expense")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    category = input("Enter category: ")
    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total = total + expense["amount"]

    print("Total spent on", category, ": Rs.", total)


def highest_expense():
    """Display the expense with the highest amount."""
    if len(expenses) == 0:
        print("No expenses found.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("Highest Expense")
    print_expense(highest)


def lowest_expense():
    """Display the expense with the lowest amount."""
    if len(expenses) == 0:
        print("No expenses found.")
        return

    lowest = expenses[0]

    for expense in expenses:
        if expense["amount"] < lowest["amount"]:
            lowest = expense

    print("Lowest Expense")
    print_expense(lowest)


def monthly_summary(expense_list):
    """Display month-wise totals (MM-YYYY) from a list of expenses."""
    if len(expense_list) == 0:
        print("No expenses in record yet.")
        return

    totals = {}

    for expense in expense_list:
        month = expense["date"][3:5]
        year = expense["date"][6:10]
        month_key = month + "-" + year

        if month_key in totals:
            totals[month_key] = totals[month_key] + expense["amount"]
        else:
            totals[month_key] = expense["amount"]

    print("Month-wise totals:")

    for month_key in totals:
        print(month_key, ": Rs.", totals[month_key])

    print()


def main():
    """Run the main menu loop."""
    while True:
        print("Personal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expense")
        print("4. Search by Category")
        print("5. Find Highest Expense")
        print("6. Find Lowest Expense")
        print("7. Monthly Summary")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_expense()
        elif choice == "5":
            highest_expense()
        elif choice == "6":
            lowest_expense()
        elif choice == "7":
            monthly_summary(expenses)
        elif choice == "8":
            print("Thank you for using Personal Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
