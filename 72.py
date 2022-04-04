# Write a program that requests five grades as input and then calculates the average after dropping the two lowest grades
grades = []
for i in range(5):
    grade = int(input("Enter one of five grades: "))
    grades.append(grade)
grades.sort()
grades = grades[2:]
average = sum(grades) / len(grades)
print("Average grade: {0:.2f}".format(average))