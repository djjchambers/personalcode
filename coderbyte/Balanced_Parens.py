arr = []

def parens(left, right, string):

		# if no more brackets can be added, then add to the final balanced string
		if left == 0 and right == 0:
			arr.append(string)
			
		# if we have a left bracket left we add it
		if left > 0:
			parens(left-1, right+1, string+'(')
			
		# if we have a right bracket left we add it
		if right > 0:
			parens(left, right-1, string+')')
			
	# the parameters parens(x, y, z) specify:
	# x: left brackets to start adding
	# y: right brackets we can add only after adding a left bracket
	# z: the string so far
	parens(3, 0, '')
	print(arr)