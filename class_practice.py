# class Triangle():
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def calculate_perimeter(self):
#         P = self.a + self.b + self.c
#         return P
#
# edge1 = int(input('Enter edge a: '))
# edge2 = int(input('Enter edge b: '))
# edge3 = int(input('Enter edge c: '))
#
# object1 = Triangle(edge1, edge2, edge3)
#
# print('The perimeter of the triangle:',object1.calculate_perimeter())

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

    def display_info(self):
        print('A polygon is a 2D shape with straight lines.')

#child classes
class Triangle(Polygon):
    def display_info(self):
        print('A triangle is a polygon with 3 edges.')
        Polygon.display_info(self)

class Quadrilateral(Polygon):
    def display_info(self):
        print('A quadrilateral is a polygon with 4 edges.')
        Polygon.display_info(self)

edge1 = int(input('Enter edge a: '))
edge2 = int(input('Enter edge b: '))
edge3 = int(input('Enter edge c: '))

edge4 = int(input('Enter edge a: '))
edge5 = int(input('Enter edge b: '))
edge6 = int(input('Enter edge c: '))
edge7 = int(input('Enter edge d: '))

T1 = Triangle([edge1, edge2, edge3])
perimeterT = T1.get_perimeter()
T1.display_info()
print('Triangle Perimeter:', perimeterT)

Q1 = Quadrilateral([edge4, edge5, edge6, edge7])
perimeterQ = Q1.get_perimeter()
Q1.display_info()
print('Quadrilateral Perimeter:',perimeterQ)


