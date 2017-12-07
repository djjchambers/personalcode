import random

a = random.sample(range(100), 20)
b = random.sample(range(100), 20)

print(a)
print(b)

c = [x for x in a for y in b if x == y]

print(c)
