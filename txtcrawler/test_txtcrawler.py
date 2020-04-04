import os
import pytest
import tempfile
from itertools import cycle
from datetime import datetime
import unittest

TESTPATH = "D:/repos/personalcode-master/personalcode/txtcrawler/textfiles"
# NB rewrite these tests with pytest's tmpdir fixture

def test_swap_backslash_for_fwdslash():
    from txtcrawler import swap_backslash_for_fwdslash
    path = TESTPATH
    expected = "D:/repos/personalcode-master/personalcode/txtcrawler/textfiles"
    assert swap_backslash_for_fwdslash(path) == expected

def test_append_slash_if_missing_in_path():
    from txtcrawler import append_slash_if_missing_in_path
    path = TESTPATH
    expected = "D:/repos/personalcode-master/personalcode/txtcrawler/textfiles/"
    assert append_slash_if_missing_in_path(path) == expected

def test_fix_path():
    from txtcrawler import fix_path
    path = "D:/repos\\personalcode-master\\personalcode/txtcrawler/textfiles"
    expected = "D:/repos/personalcode-master/personalcode/txtcrawler/textfiles/"
    assert fix_path(path) == expected
    
    
# create designated number of files in temp dir for testing, with hashtags or dummy text in them.
# this is for testing function which finds text files
# why am i testing this anyway.
# Is there a way around it?
# Isolate the function. pass a file object to the function.
# Use a context manager for the temporary directory. Loop over range of number, call function to write to file.
# Is all this functionality useful in the test suite just to test a single function?
def write_to_file(number, path='./testfiles'):
    textlist = ['#idea', '#boilerplate', 'test', 'more test']
    textitem = cycle(textlist)
    for _ in range(number):
        file = open(path + 'file'+str(_)+'.txt', 'w')
        file.write(next(textitem))
    
def test_list_text_files_in_folder():
    from txtcrawler import list_text_files_in_folder
    testnumber1 = 5
    write_to_file(testnumber1)
    filelist = list_text_files_in_folder('./testfiles')
    expected = 5
    assert len(filelist) == expected
    
def test_list_text_files_containing_hashtags():
    from txtcrawler import list_text_files_in_folder, list_text_files_containing_hashtags
    filelist = write_to_file(5)
    hashtagslist = list_text_files_containing_hashtags(filelist)
    expected = 3
    assert len(hashtagslist) == expected

# Mock file operations using unittest, pytest test will collect these subclasses
# fixture mock Google App
# work on static data

