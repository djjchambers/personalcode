# create a class called Parent
class Parent(object):
    
    # define Parent class's override function
    def override(self):
        print("PARENT altered()")
        
    # define Parent class's implicit function
    def implicit(self):
        print("PARENT implicit()")
        
    # define Parent class's altered function
    def altered(self):
        print("PARENT altered()")
  
# create a subclass of Parent called Child
class Child(Parent):
    
    # define Child class's override function - this will override the same function in the Parent class when called
    def override(self):
        print("Child override()")
        
    # define Child class's altered function - this will call the function halfway through and show the alteration happening
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")
              
# create an instance of Parent() named dad            
dad = Parent()
# create an instance of Child() named son
son = Child()
            
# call dad's implicit function
dad.implicit()
# call son's implicit function
son.implicit()

# call dad's override function              
dad.override()
# call son's override function
son.override()
              
# call dad's altered function    
dad.altered()
# call son's altered function
son.altered()