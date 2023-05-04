class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine() #an attribute which is an instance of `Engine` class
        '''
        This means that every time a new Car object is created, 
        it will also create a new Engine object as its attribute.
        '''

class Engine:
    def __init__(self):
        self.cylinders = 4
        self.horsepower = 100


'''
You can access the attributes of the Engine instance by accessing 
the engine attribute of the Car instance, like this:
'''
my_car = Car("Toyota", "Corolla")
print(my_car.engine.cylinders) # prints 4
print(my_car.engine.horsepower) # prints 100
