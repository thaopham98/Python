"""
Define a user input
"""
ui = input('Which is the correct answer for 15x8, please enter numeric value?\n'
           # 'a. 112\n'
           # 'b. 500\n'
           # 'c. 23\n'
           # 'd. 120\n'
           'Enter your answer: ')

"""
Checking the user answer
"""
while ui!=120:
    ui = int(input('You entered incorrect answer, '
                   'try again and enter numeric value: '))

print(f'You entered correct answer for 15x8={ui}.')