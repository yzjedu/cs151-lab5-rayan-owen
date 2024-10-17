# Algorithm Document
##### Purpose: This program will act as an ATM and will error check for insuficient funds or misinputs.
1. Create a variable for balance.
- Each user starts with an initial balance of 100
2. Create While loop that runs until user chooses the "exit" option
- Prompt user to input based on the options (All options will then loop back to this step after their intended code is over)
- "V" (View balance)
- "D" (Deposit)
- "W" (Withdraw)
- "E" (Exit)
- (Convert user input to uppercase so lower case and upper case are accepted inputs)
3. If user inputs "V"
- Output the variable 'balance'
- This will then loop back to the options menu. 
4. If user inputs "D"
- Prompt user to input the amount of money they want to deposit.
- If the input is 0 or less, or not a number, display message saying it's an invalid input.
- Then loop back to the options menu

- If the input is over 0 add the input to the users balance
- Print user balance
- Loop back to options
5. If user inputs "W"
- Prompt user to input the amount they want to withdraw from balance
- If input is 0 or less or not a number, output error message

- If input is over 0, check if withdraw > balance
- If withdraw > balance output "insufficient funds"
- loop back to options menu

- If balance > withdraw, subtract withdrawal from balance. (balance - withdrawal)
- Display users balance
- Loop back to options
6. If user inputs "E", output thank you message
- End loop
7. If user doesn't input "V,D,W,E"
- Display error message and loop back to step 2.
