
# The current calendar, called the Gregorian calendar, was introduced in 1582.
# Every year divisible by four was created to be a leap year, with the exception of the
# years ending in 00 (that is, those divisible by 100) and not divisible by 400. For instance,
# the years 1600 and 2000 are leap years, but 1700, 1800, and 1900 are not. Write a program that requests a year as input and states whether it is a leap year. See Fig.

year= input("Enter year or stop to exit: ")
while year.upper() != "STOP":   
  if int(year) % 400 == 0:  
      print(year,"is a leap year")
  elif int(year) % 100 == 0:
      print(year, "is not a leap year")
  elif int(year)%4 == 0:
      print(year,"is a leap year")
  else:
      print(year, "is not a leap year")
  year= input("Enter year or stop to exit: ")  