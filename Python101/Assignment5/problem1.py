"""
Creating a function that ask the user to input integers
and do a sum calculation with the input values.
"""
def calculator():
    # Asking for user input
    value1 = int(input('Enter your value 1: '))
    value2 = int(input('Enter your value 2: '))
    value3 = int(input('Enter your value 3: '))
    value4 = int(input('Enter your value 4: '))

    return value1+value2+value3+value4 # returing the results

print(calculator()) # calling the function