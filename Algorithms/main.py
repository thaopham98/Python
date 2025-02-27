class student_info:
    def __init__(self, name, age, major): #constructor
        self.name = name
        self.age = age
        self.major = major

    def display_student_info(self):
        print('\nHello, my name is', self.name , "and I'm", self.age, "years old.\nMy major is", self.major,'.')

command = input('Press "y" to continue: ') # Beginning the loop
while ( command.lower() == 'y'):
    ## User input
    name_input = input('\nPlease enter your name: ')
    age_input = input('Please enter your age: ')
    major_input = input('Please enter your majors: ')

    ## Creating an object, student1
    student1 = student_info(name_input, age_input, major_input)
    student1.display_student_info()
    command = input('\nDo you want to enter your information again? [y/n]: ')
print('\nBye!\n')