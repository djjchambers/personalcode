def numsum(numlist1):
	modifier = 1
	if numlist1[0] == numlist1[1] == numlist1[2]:
		modifier = 3
	print('sum= ', sum(numlist1))
	print('adjusted= ', modifier*(sum(numlist1)))

numbers = [1, 2, 3]
numsum(numbers)
numbers = [2, 2, 2]
numsum(numbers)
numbers = [10, 11, 12]
numsum(numbers)
numbers = [20, 20, 20]
numsum(numbers)