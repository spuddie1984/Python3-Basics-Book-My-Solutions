# Write a script that defines two functions:
# 
# 1. convert_cel_to_far() which takes one float parameter representing
#    degrees Celsius and returns a float representing the same 
#    temperature in degrees Fahrenheit using the following formula:
#       F = C * 9/5 + 32
# 
# 2. convert_far_to_cel() which take one float parameter representing
#    degrees Fahrenheit and returns a float representing the same 
#    temperature in degrees Celsius using the following formula:
#       C = (F - 32) * 5/9
# 
# The script should first prompt the user to enter a temperature in de-
# grees Fahrenheit and then display the temperature converted to Celsius.
# Then prompt the user to enter a temperature in degrees Celsius and
# display the temperature converted to Fahrenheit.
# All converted temperatures should be rounded to 2 decimal places.

# convert celsuis to fahrenheit
def convert_cel_to_far(degrees):
    temp = degrees * 9 / 5 + 32
    # round to 2 decimal places
    return f'The temperature in Fahrenheit is {temp:.2f}'    

# convert fahrenheit to celsius
def convert_far_to_cel(degrees):
    temp = (degrees - 32) * 5 / 9
    # round to 2 decimal places
    return f'The temperature in Celsius is {temp:.2f}'

user_input = float(input('Please enter a temperature in degrees fahrenheit: '))

# print first result to the console 
print(convert_far_to_cel(user_input))

# now ask user for temperature in celsius format
user_input = float(input('Please enter a temperature in degrees fahrenheit: '))

# print second result
print(convert_cel_to_far(user_input))

