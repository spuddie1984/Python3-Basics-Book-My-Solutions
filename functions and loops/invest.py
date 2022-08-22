# In this challenge, you will write a program that tracks
# the growing amount of an investment over time.
# An initial deposit, called the principal amount, is made. Each year,
# the amount increases by a fixed percentage, called the annual rate of
# return. For example, a principal amount of $100 with an annual rate of return
# of 5% increases the first year by $5. The second year, the increase is
# 5% of the new amount $105, which is $5.25.
# 
# Write a function called invest with three parameters: the principal
# amount, the annual rate of return, and the number of years to calculate.
# The function signature might look something like this:\
#       def invest(amount, rate, years):
# 
# The function then prints out the amount of the investment, rounded
# to 2 decimal places, at the end of each year for the specified number
# of years.
# 
# For example, calling invest(100, .05, 4) should print the following:
#   year 1: $105.00
#   year 2: $110.25
#   year 3: $115.76
#   year 4: $121.55

def invest(amount, rate, years):
    # to keep track of each years annual rate
    total = amount
    # keep track of which year it is
    year_counter = 1

    for year in range(years):
        # update the annual rate adding the the annual rate to each subsequent year
        total += ( total / 100 * (rate * 100))
        # print the annual rate
        print(f'year {year_counter}: ${total:.2f}')
        # move on to next year
        year_counter += 1


# invest(100, 0.05, 4)
# To finish the program, prompt the user to enter an initial amount, an
# annual percentage rate, and a number of years. Then call invest() to
# display the calculations for the values entered by the user.

user_principle_amt = float(input('Please enter the principle amount: '))

user_rate = float(input('Please enter the annual percentage rate: ')) / 100

user_years = int(input('Please enter the total years of investment'))

invest(user_principle_amt, user_rate, user_years)