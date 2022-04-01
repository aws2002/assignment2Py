# The median of an ordered set of measurements is a number separating the
# lower half from the upper half. If the number of measurements is odd, the median is
# the middle measurement. If the number of measurements is even, the median is the
# average of the two middle measurements. Write a program that requests a number n
# and a set of n measurements (not necessarily ordered) as input and then displays the
# median of the measurements. See Fig. 3.61.

howMany = int(input("How many numbers would you like to enter? "))
listOfNumbers = []
for i in range(howMany):
    num = int(input("Enter a number: "))
    listOfNumbers.append(num)
listOfNumbers.sort()
if howMany % 2 == 1:
    median = listOfNumbers[int(howMany / 2)]
else:
    m = int(howMany / 2)
    median = (listOfNumbers[m - 1] + listOfNumbers[m]) / 2
print("Median:", median)
