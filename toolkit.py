"""
SpendWise Personal Toolkit
Future Proof - Week 8 Final Project
"""

import math

# Lists for storing expenses and tasks.
expenses = []
tasks = []


# Display a formatted section heading.
def heading(title):
    print("\n" + "=" * 44)
    print(title.center(44))
    print("=" * 44)


# Safely collect numerical input from the user.
def get_number(prompt, non_negative=False):
    while True:
        try:
            number = float(input(prompt))

            if not math.isfinite(number):
                print("Please enter a finite number.")
                continue

            if non_negative and number < 0:
                print("Please enter a positive number or zero.")
                continue

            return number

        except ValueError:
            print("Invalid input. Please enter a valid number.")


# TOOL 1: Record expenses and calculate total spending.
def expense_tracker():
    while True:
        heading("EXPENSE TRACKER")

        print("1. Add expense")
        print("2. View expenses")
        print("3. View total spending")
        print("4. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter expense name: ").strip()

            if not name:
                print("Expense name cannot be empty.")
                continue

            amount = get_number(
                "Enter amount (KES): ",
                non_negative=True
            )

            expenses.append([name, amount])

            print(f"{name} added successfully!")
            print(f"Amount: KES {amount:,.2f}")

        elif choice == "2":
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("\nYour expenses:")

                for index, expense in enumerate(expenses, 1):
                    name, amount = expense
                    print(f"{index}. {name}: KES {amount:,.2f}")

        elif choice == "3":
            total = 0

            for expense in expenses:
                total += expense[1]

            print(f"Total spending: KES {total:,.2f}")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please select 1-4.")


# TOOL 2: Perform basic arithmetic calculations.
def calculator():
    heading("CALCULATOR")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Return to main menu")

    choice = input("Select an operation: ").strip()

    if choice == "5":
        return

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid operation. Please try again.")
        return

    first = get_number("Enter first number: ")
    second = get_number("Enter second number: ")

    if choice == "1":
        result = first + second
        operator = "+"

    elif choice == "2":
        result = first - second
        operator = "-"

    elif choice == "3":
        result = first * second
        operator = "*"

    else:
        if second == 0:
            print("Error: Cannot divide by zero.")
            return

        result = first / second
        operator = "/"

    print(f"Result: {first:g} {operator} {second:g} = {result:g}")


# TOOL 3: Add, view and remove personal tasks.
def todo_list():
    while True:
        heading("TO-DO LIST")

        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task = input("Enter your task: ").strip()

            if not task:
                print("Task cannot be empty.")
                continue

            tasks.append(task)
            print(f"Task '{task}' added successfully!")

        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")

                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")

                print(f"Total tasks: {len(tasks)}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
                continue

            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")

            try:
                number = int(input("Enter task number: "))

                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print(f"Task '{removed}' removed.")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid whole number.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please select 1-4.")


# TOOL 4: Compare the user's budget with recorded expenses.
def budget_planner():
    heading("BUDGET PLANNER")

    budget = get_number(
        "Enter your budget (KES): ",
        non_negative=True
    )

    total = 0

    for expense in expenses:
        total += expense[1]

    remaining = budget - total

    print("\nBUDGET SUMMARY")
    print(f"Budget:         KES {budget:,.2f}")
    print(f"Total expenses: KES {total:,.2f}")
    print(f"Balance:        KES {remaining:,.2f}")

    if remaining > 0:
        print("Great! You are within your budget.")

    elif remaining == 0:
        print("You have used your entire budget.")

    else:
        print(f"Warning: You are over budget by KES {abs(remaining):,.2f}.")


# MAIN MENU: Keep the program running until the user quits.
def main():
    print("\nWelcome to SpendWise Personal Toolkit!")
    print("Manage your money, calculations and daily tasks.")

    while True:
        heading("SPENDWISE PERSONAL TOOLKIT")

        print("1. Expense Tracker")
        print("2. Calculator")
        print("3. To-Do List")
        print("4. Budget Planner")
        print("5. Quit")
        print("=" * 44)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            expense_tracker()

        elif choice == "2":
            calculator()

        elif choice == "3":
            todo_list()

        elif choice == "4":
            budget_planner()

        elif choice == "5":
            print("\nThank you for using SpendWise!")
            print("Stay productive and spend wisely. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")


# Start the program.
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nSpendWise closed. Goodbye!")
