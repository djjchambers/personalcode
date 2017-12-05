class Other(object):
    
    def override(self):
        print("OTHER override()")
        
    def implicit(self):
        print("OTHER implicit()")
        
    def altered(self):
        print("OTHER altered()")
        
class Child(object):
    
    def __init__(self):
        # create instance of Other object and assign it to other variable
        self.other = Other()
        
    def implicit(self):
        self.other.implicit()
        
    def override(self):
        print("CHILD override()")
        
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

# create instance of Child object and assign it to son variable
son = Child()
    
# call implicit function in son
son.implicit()
son.override()
son.altered()