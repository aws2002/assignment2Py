# Second-Suit-Half-Off Sale A men’s clothing store advertises that if you buy a suit,
# you can get a second suit at half-off. What they mean is that if you buy two suits, then
# the price of the lower-cost suit is reduced by 50%. Write a program that accepts the
# two costs as input and then calculates the total cost after halving the cost of the lowest
# price suit. See Fig.



firstSuit=float(input("Enter cost of first suit:"))
secondSuit=float(input("Enter cost of second suit:"))
cost=firstSuit+(secondSuit*0.5)
print("Cost of the two suits is $",cost)