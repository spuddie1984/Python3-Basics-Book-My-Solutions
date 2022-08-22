# 1. Create a tuple literal named cardinal_numbers that holds the strings
# "first", "second", and "third", in that order.

cardinal_numbers = 'first','second','third'

# 2. Using index notation and print(), display the string at index 1 in
# cardinal_numbers.

print(cardinal_numbers[1])

# 3. In a single line of code, unpack the values in cardinal_numbers into
# three new strings named position1, position2, and position3. Then
# print each value on a separate line.

position1, position2, position3 = cardinal_numbers

# 4. Using tuple() and a string literal, create a tuple called my_name that
# contains the letters of your name.

my_name = tuple('xavier')

# 5. Check whether the character "x" is in my_name using the in keyword.

'x' in my_name

# 6. Create a new tuple containing all but the first letter in my_name using
# slice notation.

my_new_name = my_name[1:len(my_name)]
