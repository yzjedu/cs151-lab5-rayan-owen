# CS 151
# Professor Z.
# Programmers: Ray and Owen

# Create code to function as an ATM

# Constant
balance = 1000 #Users starting balance

while True:
    choice = input(
        "Please Pick an Option:\n - View Balance (V)\n - Deposit (D)\n - Withdraw (W)\n - Exit (E)\n").upper()

    if choice == "V":
        print(f"Your balance is: {balance}")

    elif choice == "D":
        cash = input("Please enter cash amount to deposit:\n")
        balance += int(cash)
        print(f"Successfully deposited! Your balance is: {balance}")

    elif choice == "W":
        cash = int(input("Please enter cash amount to withdraw:\n"))
        if cash > balance or cash < 0: #If cash withdrawn is negative or greater than balance
            print("Unable to process request: Insufficient funds")
        else:
            balance -= cash
            print(f"Successfully withdrawn! Your balance is: {balance}")

    elif choice == "E":
        print("Thank you, have a nice day!")
        break

    else:
        print("Please input V, D, W, or E")







