def decorator_italics(func):
	def wrapper():
		return '<i>' + func() + '</i>'
	return wrapper
	
def decorator_underline(func):
	def wrapper():
		return '<u>' + func() + '</u>'
	return wrapper
	
def decorator_bold(func):
	def wrapper():
		return '<b>' + func() + '</b>'
	return wrapper
	
@decorator_bold
@decorator_italics
@decorator_underline
def print_hello():
	return 'Hello'
	
print(print_hello())