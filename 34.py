# Write a program to process a savings-account withdrawal. The
# program should request the current balance and the amount of the withdrawal as
# input and then display the new balance. If the withdrawal is greater than the original
# balance, the program should display “Withdrawal denied.” If the new balance is less
# than $150, the message “Balance below $150” should also be displayed. See Fig. 3.13.


balance = float(input("Enter current balance: "))
amountOfWithdrawal = float(input("Enter amount of withdrawal: "))
if (balance >= amountOfWithdrawal):
    balance -= amountOfWithdrawal
    print("The new balance is ${0:,.2f}.".format(balance))
    if balance < 150:
        print("Balance below $150", "Warning")
else:
    print("Withdrawal denied.")    