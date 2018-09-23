class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        assert isinstance(self.length, int), 'Should be integer'
        assert isinstance(self.width, int), 'Should be integer'
        
    def get_area(self):
        return self.length * self.width
        
r = Rectangle(20, 30)
print(r.get_area())