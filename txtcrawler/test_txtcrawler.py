import os
import pytest
import tempfile
from itertools import cycle, islice
from datetime import datetime
import unittest

from txtcrawler import swap_backslash_for_fwdslash, append_slash_if_missing_in_path, fix_path, list_text_files_in_folder, list_text_files_containing_hashtags

TESTPATH = "D:/repos/personalcode-master/personalcode/txtcrawler/textfiles"

def test_swap_backslash_for_fwdslash():
    path = TESTPATH
    expected = "D:/repos/personalcode-master/personalcode/txtcrawler/textfiles"
    assert swap_backslash_for_fwdslash(path) == expected

def test_append_slash_if_missing_in_path():
    path = TESTPATH
    expected = "D:/repos/personalcode-master/personalcode/txtcrawler/textfiles/"
    assert append_slash_if_missing_in_path(path) == expected

def test_fix_path():
    path = "D:/repos\\personalcode-master\\personalcode/txtcrawler/textfiles"
    expected = "D:/repos/personalcode-master/personalcode/txtcrawler/textfiles/"
    assert fix_path(path) == expected
    
    
# create designated number of files in temp dir for testing, with hashtags or dummy text in them.
# this is for testing function which finds text files
def write_to_file(number, pathname):
    textlist = ['#idea', '#boilerplate', 'test text', 'more test text']
    textitem = islice(cycle(textlist), number)
    for i, item in enumerate(textitem):
        filename = f"file{i}.txt"
        with open(os.path.join(pathname, filename), 'w') as filetowrite:
            filetowrite.write(item)
    
def test_list_text_files_in_folder(tmpdir):
    write_to_file(5, tmpdir.dirpath())
    filelist = list_text_files_in_folder(tmpdir.dirpath())
    expected = 5
    assert len(filelist) == expected
    
def test_list_text_files_containing_hashtags(tmpdir):
    filelist = write_to_file(5, tmpdir.dirpath())
    hashtagslist = list_text_files_containing_hashtags(filelist)
    expected = 3
    assert len(hashtagslist) == expected

# Mock file operations using unittest, pytest test will collect these subclasses
# fixture mock Google App
# work on static data

