class Parent(object):
    
    def override(self):
        print("PARENT override()")
        
class Child(object):
    
    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()