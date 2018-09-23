class A():
    def __init__(self, x):
        self.x = x "using class A init"

class B(A):
    def __init__(self x):
        self.x = x "using class B init"
        
class C(A):
    def __init__(self, x):
        super.__init__(self)
        self.x = x "inherited init from A"
        
class D(C):
    def __init__(self, x):
        self.x = x "inherited C's inheritance from A, but overrode it!"
        
a = A()
print(a.x)
b = B()
print(b.x)
c = C()
print(c.x)
d = D()
print(d.x)