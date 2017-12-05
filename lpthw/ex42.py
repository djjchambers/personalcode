## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    ## ??
    def boomboom(self, name):
        print(f"I am an animal called {name}... hear my heart beat!")

## ??
class Dog(Animal):
    
    def __init__(self, name):
        ## ??
        self.name = name
        
    def woof(self, name):
        print(f"Woof! I am a goodboye named {name}!")
        
    
        
## ??
class Cat(Animal):
    
    def __init__(self, name):
        ## ??
        self.name = name
        
    def meow(self, name):
        print(f"Meow, I am a cat called {name}.")
        
## ??
class Person(object):
    
    def __init__(self, name):
        ## ??
        self.name = name
        ## person has-a pet of some kind
        self.pet = None
        
    def harumph(self, name):
        print(f"Harumph, I am {name} the person.")
        
## ??
class Employee(Person):
    
    def __init__(self, name, salary):
        ## ?? (hm what is this strange magic?)
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary
        
    def yawn(self, name, salary):
        print(f"Yawn, I am an employee named {name}, who makes only {salary}.")

## ??
class Fish(object):
    
    ## create function blurble that takes param self
    def blurble(self, name):
        print(f"Blurble! I am a fish called {name}!")

## ??
class Salmon(Fish):
    ## ??
    def leap(self, name):
        print(f"Watch {name} leap!")

## ??
class Halibut(Fish):
    def sizzle(self, name):
        print(f"Whoosh - watch {name} fry!")

## Rover is-a Dog
rover = Dog("Rover")
rover.boomboom("Rover")
rover.woof("Rover")

## ??
catname = "Satan"
satan = Cat("Satan")
satan.boomboom(catname)
satan.meow(catname)

## set mary to an instance of class Person with argument "Mary"
mary = Person("Mary", )
## from mary, get the harumph function and call it with argument "Mary"
mary.harumph("Mary")

## OK this bit is a little beyond me now. I can understand it literally...
## from mary get the pet instance attribute, set it to satan
## trying to set a dictionary and map the attribute names/values from dict
mary.pet = rover

## set frank to an instance of Employee using the argument "Frank" and 120000
frank = Employee("Frank", 120000)
## from frank get the function yawn, call it using the argument "Frank" and 120000
frank.yawn("Frank", 120000)

## from frank get the pet attribute and set it to rover
frank.pet = rover

## ??
flipper = Fish()
flipper.blurble("Flipper")

## ??
crouse = Salmon()
crouse.blurble("Crouse")
crouse.leap("Crouse")

## ??
harry = Halibut()
harry.blurble("Harry")
harry.sizzle("Harry")