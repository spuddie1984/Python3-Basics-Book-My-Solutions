# Write a script that receives two numbers from the
# user and displays the first number raised to the power of the second
# number.

# get the base number convert it to a float
base = float(input('Enter a base: '))

# same with the exponent number
exponent = float(input('Enter a exponent: '))

# print a string with the base num and exponent and the result of the 2 numbers
print(f"{base} to the power of {exponent} = {base ** exponent}")