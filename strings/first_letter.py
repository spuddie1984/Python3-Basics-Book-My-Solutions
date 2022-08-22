# Write a script that first prompts the user for input by using the string
# "Tell me your password". The script should then determine the first letter of the 
# user's input, convert that letter to upper-case and display it back


# ask for user input then go to new line
user_response = input( 'Tell me your password\n' )
try:
    print(f'The first letter you entered was: {user_response[0].upper()}')
except:
    print('Please enter a word other then a number')