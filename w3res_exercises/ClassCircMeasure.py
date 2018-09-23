import math

class Circle():
    def __init__(self, radius):
        self.radius = radius
        
    def get_area(self):
        n = math.pi * self.radius
        return n*n
        
    def get_circumf(self):
        return math.pi * self.radius * 2
        
c = Circle(2)
print('area=', c.get_area())
print('circumference=', c.get_circumf())