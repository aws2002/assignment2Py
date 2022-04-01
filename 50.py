# Write a program that requests the numeric grades on a midterm
# and a final exam and then uses a function named semesterGrade to assign a semester
# grade (A, B, C, D, or F). The final exam should count twice as much as the midterm exam, the semester average should be rounded up to the nearest whole number, and the semester grade should be assigned by the following criteria: 90–100 (A),
# 80–89 (B), . . . . See Fig. 4.12. The function semesterGrade should call a function named
# ceil that rounds noninteger numbers up to the next integer

import math
midterm = int(input("Enter grade on midterm: "))
finalGrade = int(input("Enter grade on final exam: "))

def semesterGrade(mid, final):
   final = final * mid
   math.ceil(final)
   if (final > 90): 
        return "A"
   elif (final > 80): 
        return "B"
   elif (final > 70):
        return "C"
   elif (final > 60):
        return "D"
   else:
        return "F"

print("Semester grade: ", semesterGrade(midterm, finalGrade))
        