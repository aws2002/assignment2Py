# Write a program that asks the user to enter a single uppercase letter and then informs the user if they didn’t comply with the request.

uppercaseLetter=input("Enter a single uppercase letter:")
if(uppercaseLetter.isupper==True):
    print("You did not comply with the request.")
else:
    print("You did comply with the request.")    
