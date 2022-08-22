# 1. Create an empty dictionary named captains.

captains = {}

# 2. Using square bracket notation, enter the following data into the
# dictionary one item at a time:
# • 'Enterprise': 'Picard'
# • 'Voyager': 'Janeway'
# • 'Defiant': 'Sisko'

captains['Enterprise'] = 'Picard'
captains['Voyager'] = 'Janeway'
captains['Defiant'] = 'Sisko'

# 3. Write two if statements that check if "Enterprise" and "Discovery"
# exist as keys in the dictionary. Set their values to "unknown" if the
# key does not exist.

if "Enterprise" not in captains:
    captains['Enterprise'] = 'unknown'

if "Discovery" not in captains:
    captains['Discovery'] = 'unknown'

# 4. Write a for loop to display the ship and captain names contained
# in the dictionary. For example, the output should look something
# like this:
# The Enterprise is captained by Picard.

for ship,captain in captains.items():
    print(f'The {ship} is captained by {captain}')

# 5. Delete "Discovery" from the dictionary.

del captains['Discovery']

# 6. Bonus: Make the same dictionary by using dict() and passing in
# the initial values when you first create the dictionary.

captains = dict(Enterprise = 'Picard',Voyager = 'Janeway',Defiant = 'Sisko')
print(captains)