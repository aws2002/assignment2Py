# Write a program that requests a word as input and counts the
# number of different vowels in the word

word = input("Enter a word: ")
word = word.upper()
vowels = "AEIOU"
vowelsFound = []
numVowels = 0
for letter in word:
    if (letter in vowels) and (letter not in vowelsFound):
        numVowels += 1
        vowelsFound.append(letter)
print("Number of vowels:", numVowels)