import math

def sum_all(nums):
	L = [int(num) for num in nums.split(',')]
	return sum(L)
	
def mult_all(nums):
	L = [int(num) for num in nums.split(',')]
	x = 1
	for y in L:
		x *= y
	return x
	
def rev_str(S):
	rev_s = S[::-1]
	return rev_s
	
def calc_fact(num):
	return math.factorial(num)
	
def num_in_range(num, low, high):
	return int(low) < int(num) < int(high)
	
def calc_upper_lower(str):
	upc = 0
	loc = 0
	for char in str:
		if char.isupper():
			upc += 1
		elif char.islower():
			loc += 1
	return ('{0}, {1}'.format(upc, loc))