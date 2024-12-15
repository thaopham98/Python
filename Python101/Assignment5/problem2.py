'''
    Create a dict that store course's codes and numbers,
    the user must enter the course code in integer to get
    the full course name.
'''

''' A distionary container'''
courses = {
    230:'MSBA 230 Database Management System with SQL and R',
    232:'MSBA 232 Programming for Data Science',
    265:'MSBA 265 Special Analytics Topics'
}

''' Create a while loop ask for user input and check if the input is correct or not.
    If correct, display the key's value and break the loop.
    If not, display a message and the loop continue to run. 
'''
while True:
    x = int(input(f'{courses.keys()} \nEnter a key in course: ')) # Asking the user to enter an integer

    '''Checking for if the input in dict or not'''
    if x in courses.keys():
        print(courses[x]) # display the full course name if the input is matched with one of the keys.
        break
    else:
        print('Invalid input\n') # display an error message if the input is not matched.