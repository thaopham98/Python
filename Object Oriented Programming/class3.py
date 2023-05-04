'''
Abstraction & Inheritance
'''

'''Abstract class for shapes'''
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    def draw(self):
        pass


'''
"Shape" is an abstract class that defines a set of properties 
and methods that are common to all shapes, 
while "Circle", "Square", and "Triangle" are concrete classes 
that inherit properties and methods from "Shape" and provide 
their own implementation for specific features.
'''
# Concrete class for circles
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def draw(self):
        # code to draw a circle
        pass
        
# Concrete class for squares
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
    
    def draw(self):
        # code to draw a square
        pass
        
# Concrete class for triangles
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        # code to calculate the perimeter of a triangle
        pass
        
    def draw(self):
        # code to draw a triangle
        pass
