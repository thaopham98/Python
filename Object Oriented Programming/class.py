from datetime import date

class Student:
    
    def __init__(self):
        self.name = input('\nEnter your name: ')
        self.major = input('Enter your major: ')
        self.birthyear = int(input('Enter your year of birth: '))
        # self.curYear = int(input('Enter the current year: '))
        

    def cal_stu_age(self): #calculating the student's age using birthday
        todays_date = date.today()
        return todays_date.year - self.birthyear


    def studentINFO(self): #printing out the student's info
        print('\nStudent name:', self.name)
        print('Student major:', self.major)
        print('Student birthyear:', self.birthyear)
        print('Student age:', self.cal_stu_age(), '\n\n')


#Creating an object 
student1 = Student()
student1.studentINFO()

#Creating an object 
student2 = Student()
student2.studentINFO()