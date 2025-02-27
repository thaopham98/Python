import random
import string 
"""Decide on the criteria for the password"""

"""Validating if the user enters 'y' or 'n' for the first 4 criterias or not. """
def validate_str_input(inputs):
    while (inputs.lower() != 'y') and (inputs.lower() != 'n'): # Only stop when user input 'y' or 'n' or 'Y' or 'N'
        inputs = input('Incorrect input, please try again: ')
    return inputs

"""Validating if the user enter an integer for the 5th criteria or not. """
def validate_int_input(usr_input):
    while not usr_input.isdigit(): # Only stop when user input an int number
        usr_input = input('Incorrect input, please enter an int: ')
    return usr_input

"""Asking the user to enter the criteria for the password"""
def userCriteria():
    usrCriterias = {'1. Uppercase': None, 
                    '2. Lowercase': None,
                    '3. Number': None,
                    '4. Special characters': None,
                    '5. Password length': None}
    
    print('\nPlease enter your criterias')

    usrCriterias['1. Uppercase'] = validate_str_input(input('Do you want uppercase letters? Please enter y/n: '))

    usrCriterias['2. Lowercase'] = validate_str_input(input('Do you want lowercase letters? Please enter y/n: '))
    
    usrCriterias['3. Number'] = validate_str_input(input('Do you want numbers? Please enter y/n: '))

    usrCriterias['4. Special characters'] = validate_str_input(input('Do you want special characters (e.g., !, @, #, $)? Please enter y/n: '))

    '''
    Checking if the user input an int or not, 
    then convert the input, which currently
    a string into an int.
    '''
    usrCriterias['5. Password length'] = int(validate_int_input(input('How long do you want your password to be? Please enter an int number: ')))

    """Displaying user inputs for each criterias"""
    # for key, value in usrCriterias.items():
    #     print(f'{key}: {value}\n')

    return usrCriterias

"""BASED ON THE USER'S CRITERIAS, GENERATE THE PASSWORD"""
def generate_password(criteria):
    """Generates a password based on the user's criterias."""

    '''
    Using the extend() to add the user's criterias to a list
    '''

    characters = []
    if criteria["1. Uppercase"]:
        characters.extend(string.ascii_uppercase) # adding all the uppercase letters to a list

    if criteria["2. Lowercase"]:
        characters.extend(string.ascii_lowercase) # adding all the lowercase letters to a list

    if criteria["3. Number"]:
        characters.extend(string.digits) # adding all the digits to a list

    if criteria["4. Special characters"]:
        characters.extend(string.punctuation) # adding all the punctuations to a list

    password = ""
    for i in range(criteria["5. Password length"]):
        # print(f'password[{i}]: {password[i]}')
        password += random.choice(characters) 

    return password

def main():
  """Main function."""
  criteria = userCriteria()
  password = generate_password(criteria)
  print("Your password is: " + password)

if __name__ == "__main__":
  main()