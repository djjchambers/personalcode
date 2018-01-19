import pytest
from func_exercise_bonanza import *

def test_sum_all():
	assert sum_all('1, 2, 3') == 6
	
def test_mult_all():
	assert mult_all('4, 5, -6') == -120
	
def test_rev_str():
	assert rev_str('abc123') == '321cba'
	
def test_calc_fact():
	assert calc_fact(4) == 24
	
def test_num_in_range():
	assert num_in_range(2, 0, 3) == True
	
def test_calc_upper_lower():
	assert calc_upper_lower('Hello Sailor') == '2, 9'
	
def test_list_unique():
	assert list_unique([1, 2, 2, 2, 3]) == [1, 2, 3]
	
def test_is_prime():
	assert is_prime(7) == True
	assert is_prime(23) == True
	assert is_prime(100) == False

def test_even_from_list():
	assert even_from_list([1, 2, 2, 3, 4, 5, 6, 7, 8]) == [2, 2, 4, 6, 8]
	
def test_is_perfect():
	assert is_perfect(6) == True
	assert is_perfect(12) == False
	assert is_perfect(496) == True
	
def test_is_palindrome():
	assert is_palindrome('rotator') == True
	assert is_palindrome('madam') == True
	assert is_palindrome('biscuit') == False
	
def test_pascal_triangle():
	assert pascal_triangle(5) == 14641
	assert pascal_triangle(1) == 1
	assert pascal_triangle(6) == 15101051
	
def test_is_pangram():
	assert is_pangram('The quick brown fox jumps over the lazy dog') == 'Yes'
	assert is_pangram('How vexingly quick daft zebras jump!') == 'Yes'
	assert is_pangram('Arseholes and elbows') == 'No'
	
def test_ordered_hyphenated():
	assert ordered_hyphenated('bog-beef-baby-disease') == 'baby-beef-bog-disease'
	
def test_list_sq():
	assert list_sq() == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
	
def test_decorator_chain():
	assert decorator_chain('hello') == '<b><i><u>hello</u></i></b>'

def test_string_executor():
	assert string_executor("print('hello')") == 'hello'