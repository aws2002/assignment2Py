# Write a menu-driven program that allows the user to make transactions to a savings account. Assume that the account initially has a balance of $1,000.
# See Fig. 3.43.


balance=1000 
print("1. Make a Deposit")
print("2. Make a Withdrawal") 
print("3. Obtain Balance")
print("4. Quit")

while True:
    selection= int(input("Make a selection from the options menu:"))
    match selection:
        case 1:
            balance=float(input("Enter amount of deposit :"))+balance
            print("Deposit Processed.")
        case 2:
            withdrawal=float(input("Enter amount of withdrawal:"))
            if(balance>withdrawal):
                balance=balance-withdrawal
                print("Withdrawal Processed.")
            else:
                print("Denied. Maximum withdrawal is $",balance)
                withdrawal=float(input("Enter amount of withdrawal:"))
                balance=balance-withdrawal
                print("Withdrawal Processed.")
        case 3:
            print("Balance:$",balance)
        case 4:
            break
        case _:
            print("Something's wrong selection") 

            