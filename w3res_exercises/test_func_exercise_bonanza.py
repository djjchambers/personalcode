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