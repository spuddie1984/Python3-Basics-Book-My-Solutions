# 1. Create a list named food with two elements, "rice" and "beans".

food = ['rice','beans']

# 2. Append the string "broccoli" to food using .append().

food.append('broccoli')

# 3. Add the strings "bread" and "pizza" to food using .extend().

food.extend(['bread','pizza'])

# 4. Print the first two items in the food list using print() and slice no-
# tation.

print(food[0:2])

# 5. Print the last item in food using print() and index notation.

print(food[-1])

# 6. Create a list called breakfast from the string "eggs, fruit, orange
# juice" using the string .split() method.

breakfast = "eggs, fruit, orange juice".split(',')
print(breakfast)

# 7. Verify that breakfast has three items using len().

print(len(breakfast))

# 8. Create a new list called lengths using a list comprehension that con-
# tains the lengths of each string in the breakfast list.

print([len(string) 
        for string in breakfast])