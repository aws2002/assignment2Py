# A supermarket sells apples for $2.50 per pound. Write a cashier’s
# program that requests the number of pounds and the amount of cash tendered as
# input and displays the change from the transaction. If the cash is not enough, the
# message “You owe $x.xx more.” should be displayed, where $x.xx is the difference
# between the total cost and the cash. See Fig. 3.12 on the previous page.


weight=float(input("Enter weight in pounds:"))
payment=float(input("Enter payment in dollars:"))
amount=weight*2.5
if(amount<=payment):
    print("Your change is $",payment-amount)
else:
    print("You owe $",abs(payment-amount)," more")   