'''
the program askes for an integer input from the user
and checks if the input data type is correct or not.
it will ask the user to enter the integer infinitely if it finds
the input is incorrect.
'''

while True: # setting the while to true, the loop will run infinitely
    try: # `try` will test the user input
        userInput = int(input("Enter your student number: ")) # `int()` accepts integer input
        break # stop the while loop if the input is the correct data type
    except ValueError: # `except` catches invalid input data type.
        print('Invalid input, please enter an integer.') # display error message to the user
print(f'Your student number is {userInput}') # display correct user input