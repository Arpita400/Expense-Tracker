# Expense Tracker Application

expenses = []

# ---------------- Add Expense ----------------
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/etc): ")
    note = input("Enter note: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses.append(expense)
    print("Expense added successfully!")


# ---------------- View Expenses ----------------
def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses):
        print(f"{i+1}. Amount: {exp['amount']}, Category: {exp['category']}, Note: {exp['note']}")


# ---------------- Update Expense ----------------
def update_expense():
    view_expenses()
    if not expenses:
        return

    index = int(input("Enter expense number to update: ")) - 1

    if 0 <= index < len(expenses):
        amount = float(input("Enter new amount: "))
        category = input("Enter new category: ")
        note = input("Enter new note: ")

        expenses[index] = {
            "amount": amount,
            "category": category,
            "note": note
        }
        print("Expense updated successfully!")
    else:
        print("Invalid index!")


# ---------------- Delete Expense ----------------
def delete_expense():
    view_expenses()
    if not expenses:
        return

    index = int(input("Enter expense number to delete: ")) - 1

    if 0 <= index < len(expenses):
        expenses.pop(index)
        print("Expense deleted successfully!")
    else:
        print("Invalid index!")


# ---------------- Total Spending ----------------
def total_spending():
    total = sum(exp["amount"] for exp in expenses)
    print("Total Spending:", total)


# ---------------- Category-wise Spending ----------------
def category_spending():
    summary = {}

    for exp in expenses:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"]

    print("\n--- Category-wise Spending ---")
    for cat, amt in summary.items():
        print(f"{cat}: {amt}")


# ---------------- Main Menu ----------------
def main():
    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Total Spending")
        print("6. Category-wise Spending")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            update_expense()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            total_spending()
        elif choice == '6':
            category_spending()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

main()
        