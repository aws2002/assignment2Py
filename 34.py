# Write a program to process a savings-account withdrawal. The
# program should request the current balance and the amount of the withdrawal as
# input and then display the new balance. If the withdrawal is greater than the original
# balance, the program should display “Withdrawal denied.” If the new balance is less
# than $150, the message “Balance below $150” should also be displayed. See Fig. 3.13.



balance=float(input("Enter current balance:"))
withdrawal=float(input("Enter amount of withdrawal:"))
amount=balance-withdrawal
if(amount<0):
    print("Withdrawal denied")
else:
    print("The new balance is $",amount)    