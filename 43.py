# The flowchart in Fig. 3.21 on the next page calculates a person’s state
# income tax. Write a program corresponding to the flowchart. See Fig. 3.20.


taxableIncome=float(input("Enter your taxable income:"))

if(taxableIncome<=20000):
    print("Your tax is $",.02 *taxableIncome)
else:
    if(taxableIncome<=50000):
        print("Your tax is $",400 + .035 *(taxableIncome - 50000))
    else:
        print("Your tax is $",1150 + .035 *(taxableIncome - 50000))

     

