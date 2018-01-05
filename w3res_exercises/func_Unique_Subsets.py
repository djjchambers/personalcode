import itertools

class UniqSub():
  
  def getprod(L):
    numstr = []
    for num in L:
      numstr.append(num)
    print(numstr)
    for i in itertools.product(numstr):
      print(i)
      
L = (list(input()))
uniquesubset = UniqSub.getprod(L)
print(uniquesubset)