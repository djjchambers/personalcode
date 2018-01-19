def g():
	print("Hi, it's me, 'g'")
	print("Thanks for calling me")
	
def f(func):
	print("Hi, it's me, 'f'")
	print("Now I will call 'func'")
	func()
	print("PS, func's real name is " + func.__name__)
	
f(g)