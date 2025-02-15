print("Welcome to your financial manager checker")

income = 0
expenses = {}

salary = int(input("What is your total income for the month: "))

income = salary

while True:
    user_input = input("Enter expense name (or type 'done' to finish): ")

    if user_input != "done":
        amount = int(input("Enter the amount of the expense: "))
        expenses.update({user_input: amount})
    else:
        total_expense = 0
        for key in expenses.values():
            total_expense += key

        result = income - total_expense

        print("--- Summary ---")
        print(f"Total income: ${income}")
        print(f"Total expenses: ${total_expense}")
        print(f"Remaining Balance: ${result}")
        
        if result < 0:
            print("You have exceeded your monthly expenses.")
        else:
            print("Congratulations. You managed you money well.")
        break