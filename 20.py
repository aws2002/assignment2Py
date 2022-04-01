# The world population reached 7 billion people on October 21,
# 2011, and was growing at the rate of 1.1% each year. Assuming that the population
# continues to grow at the same rate, approximately when will the population reach
# 8 billion? See Fig. 3.32

year=2011
population=7
rate=.011
while True:
    population*=(1+rate)
    year+=1
    if population>=8:
        break
print("Population will exceed 8 billion by year ",year)    