# Write a program that asks the user to enter a single uppercase letter and then informs the user if they didn’t comply with the request.

letter = input("Enter a single uppercase letter: ")
if (len(letter) != 1) or (letter != letter.upper()):
    print("You did not comply with the request.")  
