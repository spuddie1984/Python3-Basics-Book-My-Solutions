# Write a script that asks the user for some input with the following Prompt
# "Enter some text". Then use the .replace() method to convert the text entered 
# by the user into leetspeak by making the following changes to lower-case letters
# - the letter 'a' becomes 4
# - the letter 'b' becomes 8
# - the letter 'e' becomes 3
# - the letter 'l' becomes 1
# - the letter 'o' becomes 0
# - the letter 's' becomes 5
# - the letter 't' becomes 7
# Your program should then display the resulting string as output like below:
# Enter some text: I like to eat eggs and spam
# I lik3 70 347 3gg5 4nd 5p4m 

# grab the users input
user_input = input('Enter some text: ')

# use replace to convert the sentence into leetspeak
user_input = user_input.replace('a', '4')
user_input = user_input.replace('b', '8')
user_input = user_input.replace('e', '3')
user_input = user_input.replace('l', '1')
user_input = user_input.replace('o', '0')
user_input = user_input.replace('s', '5')
user_input = user_input.replace('t', '7')

# print out the string
print(user_input)