# Write a program that displays the values in the list numbers in descending
# order sorted by their last digit.

 ## Sort numbers in descending order by their last digit.
numbers = [865, 1169, 1208, 1243, 290]

def lastDigit(num):
    return str(num)[-1]

numbers.sort(key=lastDigit, reverse=True)
print("Sorted by last digit:")
print(numbers)







