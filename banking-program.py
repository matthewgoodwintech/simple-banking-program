# Matthew Goodwin
# Simple Banking Program
# Beginner Python Project
# Created while learning Python fundamentals# Simple Banking Program

balance = 0.0

while True:
    print("\nSimple Banking Program")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Your balance is", balance)

    elif choice == "2":
        deposit = float(input("Enter deposit amount: "))
        balance = balance + deposit
        print("Your new balance is", balance)

    elif choice == "3":
        withdraw = float(input("Enter withdraw amount: "))

        if withdraw > balance:
            print("Insufficient funds")
        else:
            balance = balance - withdraw
            print("Your new balance is", balance)

    elif choice == "4":
        print("Thank you for using the banking program.")
        break

    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")

