'''x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    print(guess)
    if abs(guess**2 -x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print(guess)
    print('failed')
else:
    print(guess)
    print('succeeded: ' + str(guess))
'''
	
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
        print(guess)
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print(guess)
    print('failed')
else:
    print(guess)
    print('succeeded: ' + str(guess))