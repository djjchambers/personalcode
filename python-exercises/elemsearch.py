def binsearch(number, numbers):
	startpoint = 0
	endpoint = len(numbers)
	while True:
		midpoint = (endpoint - startpoint) // 2
		print(startpoint, midpoint, endpoint)
		midnum = numbers[midpoint]
		print(midnum)
		if midpoint < startpoint or midpoint > endpoint or midpoint < 0:
			return ('It ain\'t there!')
		if midnum == number:
			return('Found it!')
		elif midnum < number:
			endpoint = midpoint
		else:
			startpoint = midpoint

if __name__=='__main__':
	unsortnums = [1,1,1,1,2,2,2,2,2,33,3,4,4,44,5,6,10,9,3,4,5,6,3,67,4,78,4,4,4,6,7]
	nums = sorted(unsortnums)
	num = int(input('Number to search for: '))

	print(binsearch(num, nums))