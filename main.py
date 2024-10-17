# CS 151
# Professor Z.
# Programmers: Ray and Owen

# Create code to function as an ATM

# Constant
balance = 1000 #Users starting balance


while True:
    # Prompt user to choose an option and convert it to uppercase
    choice = input(
        "Please Pick an Option:\n - View Balance (V)\n - Deposit (D)\n - Withdraw (W)\n - Exit (E)\n").upper()

    if choice == "V":
        # Display current balance
        print(f"Your balance is: {balance}")
    elif choice == "D":
        # Prompt user for deposit amount
        cash = input("Please enter cash amount to deposit:\n")
        if not cash.isdigit():
            # Check if input is a valid positive number
            print("Invalid input. Please enter a valid positive number.")
        else:
            cash = int(cash)  # Convert cash to integer after checking it's a valid number
            if cash < 0:
                # Prevent negative deposit
                print("You cannot deposit negative cash")
            else:
                balance += cash  # Update balance
                print(f"Successfully deposited! Your balance is: {balance}")

    if choice == "W":
        # Prompt user for withdrawal amount
        cash = int(input("Please enter cash amount to withdraw:\n"))
        if cash > balance : #If cash withdrawn is negative or greater than balance
            print("Unable to process request: Insufficient funds")
        elif cash < 0:
            # Prevent negative withdrawal
            print("You cannot withdraw negative cash")
        else:
            balance -= cash # Update balance after withdrawal
            print(f"Successfully withdrawn! Your balance is: {balance}")

    elif choice == "E":
        # Thank the user and exit the loop
        print("Thank you, have a nice day!")
        break

    else:
        # Handle invalid input
        print("Please input V, D, W, or E")







