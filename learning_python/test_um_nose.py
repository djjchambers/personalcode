from unnecessary_math import multiply
from nose import with_setup

def test_numbers_3_4():
    assert multiply(3, 4) == 12
    
def test_strings_a_3():
    assert multiply('a', 3) == 'aaa'
    
def my_setup_function():
    pass

def my_teardown_function():
    pass

@with_setup(my_setup_function, my_teardown_function)
def test_numbers_3_4():
    assert multiply(3, 4) == 12