import random
# '''GET & SET'''
# class Die:

#     def __init__(self):
#         self.__value = 1
    
#     def getValue(self): # gets the value from __value and returns it
#         return self.__value

#     def setValue(self, value): # sets the value from__value
#         if value < 1 or value > 6:
#             raise ValueError("Die value must be from 1 to 6.")
#         else:
#             self.__value = value

#     def roll(self):
#         self.__value = random.randrange(1,7)

# die = Die()
# value1 = int(input('Enter a value from 1 to 6: '))
# die.setValue(value1)
# print('\nDie:', die.getValue())

# '''@PROPERTIES'''
# class Die1:
#     def __init__(self):
#         self.__value = 1
    
#     # @property: getter method for the property
#     @property
#     def value(self):
#         return self.__value

#     # @propertyname.setter: settter method for the property
#     @value.setter
#     def value(self, value):
#         if value < 1 or value > 6:
#             raise ValueError("Die value must be from 1 to 6.")
#         else:
#             self.__value = value

# die1 = Die1()
# die1.value = 3
# print('\nDie:', die1.value)

'''ENCAPSULATION: READ-ONLY PROPERTY'''
class Die2:
    def __init__(self) -> None:
        self.__value = 1
    
    @property #READ-ONLY
    def value(self):
        return self.__value
    
    def roll(self):
        self.__value = random.randrange(1,7)

class Dice:
    def __init__(self) -> None:
        self.__list = []
    
    @property #READ-ONLY
    def list(self):
        dice_tuple = tuple(self.__list)
        return dice_tuple
    
    def addDice(self, die):
        self.__list.append(die)
    
    def rollAll(self):
        for die in self.__list:
            die.roll()

