import math
import string

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
	
def list_unique(L):
	S = set()
	for element in L:
		S.add(element)
	return list(S)
	
def is_prime(num):
	print("curveball!")
	for i in range(2, num):
		if num % i == 0:
			return False
	return True
	
def even_from_list(L):
	res = []
	for element in L:
		if element % 2 == 0:
			res.append(element)
	return res
	
def is_perfect(num):
	L = []
	for i in range(1, num):
		if num % i == 0:
			L.append(i)
	print(L)
	if sum(L) == num:
		return True
	else:
		return False
		
def is_palindrome(str):
	if str[::-1] == str:
		return True
	else:
		return False
		
def pascal_triangle(num):
	def pascal(col, row):
		if col == 0 or col == row:
			return 1
		else:
			return (pascal(col-1, row-1) + pascal(col, row-1))
			
	L = []
	NL = []
	for r in range(num):
		for c in range(r + 1):
			L.append(pascal(c, r))
		NL.append(L)
		L = []
	return int(''.join(map(str, NL[-1])))
	
def is_pangram(stuff):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	joined = ''.join([x for x in stuff.lower().strip() if x.isalpha()])
	print(joined)
	for char in alphabet:
		if not char in joined:
			return 'No'
	return 'Yes'
	
def ordered_hyphenated(words):
	return '-'.join(sorted(words.split('-')))
	
def list_sq():
	return [x**2 for x in range(1, 31)]

def decorator_chain(text):
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
	def print_text():
		return text

	return print_text()

def string_executor(stuff):
	eval(stuff)