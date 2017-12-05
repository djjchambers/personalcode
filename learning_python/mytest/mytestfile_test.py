# File = mytestfile_test.py

from mytest import mytestfile

def test_myfunc():
    assert mytestfile.func(1, 2) == [2, 3, -1]