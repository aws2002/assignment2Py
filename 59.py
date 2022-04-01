# Write a program that displays the values in the list numbers in ascending order sorted by their largest prime factor. Consult the flowchart in Fig. 3.30 of
# Section 3.3. See Fig. 4.21.

def main():
 ## Sort numbers by largest prime factor.
    numbers = [865, 1169, 1208, 1243, 290]
    numbers.sort(key=largestPrimeFactor)
    print("Sorted by largest prime factor:")
    print(numbers)

def largestPrimeFactor(num):
    n = num
    f = 2
    max = 1
    while n > 1:
        if n % f == 0:
            n = int(n / f)
            if f > max:
                max = f
        else:
            f += 1
    return max
main()
