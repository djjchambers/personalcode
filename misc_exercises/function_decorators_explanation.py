def getTalk(kind='shout'):

	#We define functions on the fly
	def shout(word='yes'):
		return word.capitalize()+'!'
		
	def whisper(word='yes'):
		return word.lower()+'...'
		
	# Then we return one of them
	if kind == 'shout':
		# We don't use '()' - we're not calling the function,
		# We're returning the function object
		return shout
	else:
		return whisper
		
def doSomethingBefore(func):
	print('I do something before calling the function')
	print(func())
	
scream = shout()
	
doSomethingBefore(scream)
# outputs
# I do something before calling the function
# Yes!

# How do you use this strange beast?

# Get the function and assign it to a variable
talk = getTalk()

# You can see that 'talk' here is a function object:
print(talk)
# outputs : <function shout at 0x blahdey blah>

# The object is the one returned by the function:
print(talk())
# outputs Yes!

# And you can use it directly if you feel wild:
print(getTalk('whisper')())
# outputs : yes...