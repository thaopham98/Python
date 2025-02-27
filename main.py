class StudentInfor:
    def Print(self):
        if len(self.name) <= 0:
            return 'Name is empty.'
        else:
            if self.grade == 100:
                return True
            else:
                print('Your name:',self.name)
                return False

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


#Creating an object and attributes without init.
# student1 = StudentInfor()
# student1.name = 'Thao Pham'
# student1.grade = 100
# print(student1.Print())

#Creating an object and attributes without init.
# student2 = StudentInfor()
# student2.name = input('Please enter your name for the 2nd object:')
# student2.grade = input('Please enter your grade:')
# print(student2.Print())

student3 = StudentInfor('Thao Pham', 100)
print(student3.name)
print(student3.grade)
print(student3.Print())

print(type(StudentInfor))
print(student3.__dict__)
print(student3.__module__)

print('\n###################################\nInheritance: inherit attributes and methods from a parent clas to child class')
class Animal: #Creating a parent class
    def speak(self):
        print('This animal can', end=' ')

class Dog(Animal): #creating a child class
    def bark(self):
        print('bark')

class Cat(Animal): #creating a child class
    def meow(self):
        print('meow')

dog1 = Dog() #Creating object of Dog()
dog1.speak()
dog1.bark()

cat1 = Cat()
cat1.speak()
cat1.meow()

