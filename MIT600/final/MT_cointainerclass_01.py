class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
        
class Bag(Container):
    def remove(self, e):
        '''
        assumes e is hashable
        If e occurs in self, reduces number of times by 1.
        Otherwise does nothing.
        '''
        if self.vals.get(e, 0) > 0:
            self.vals[e] -= 1
        else:
            self.vals[e] = 0
        
    def count(self, e):
        '''
        assumes e is hashable
        Returns no of times e in self.
        '''
        return self.vals.get(e, 0)
        
d1 = Bag()
d1.insert(4)
d1.insert(4)
print(d1)
d1.remove(2)
print(d1)