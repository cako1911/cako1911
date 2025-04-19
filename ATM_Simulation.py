import math 

balance = 6000

while True:
    print("""
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit
    """)

    choice = input("Please enter a selection (1-4): ")

    if choice == "1":
        print("Your current balance is:", balance)

    elif choice == "2":
        deposit = int(input("Please enter the amount you want to deposit: "))
        if deposit > 0:
            balance += deposit
            print("Updated balance:", balance)
        else:
            print("Invalid amount!")

    elif choice == "3":
        withdraw = int(input("Please enter the amount you want to withdraw: "))
        if withdraw > 0:
            if withdraw > balance:
                print("Insufficient funds. Current balance:", balance, "TL")
            else:
                balance -= withdraw
                print("Updated balance:", balance)
        else:
            print("Invalid amount!")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid selection, please enter a number between 1 and 4.")
