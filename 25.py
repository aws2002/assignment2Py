# Suppose the max function for a list didn’t exist. Define a function
# that returns the maximum value in a list of numbers.


def highestNumber(l):
    myMax = l[0]
    for num in l:
        if myMax < num:
            myMax = num
    return myMax

print (highestNumber ([77,48,19,17,93,90]))