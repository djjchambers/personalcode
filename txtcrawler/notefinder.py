# txtcrawler finds new txt files, which it disassembles according to hashtags
# contained in paragraphs
# tags are: to-do, research, ideas, boilerplate blurb, interesting quotes
# to-do gets sent to Todoist via their API
# research or quotes goes to Google Keep via API
# ideas goes to a master txt file on the Desktop
# retaining extra trailing tags in the paragraph for search purposes
# boilerplate similarly gets collated into separate files in Templates folder

import os
from datetime import datetime
from typing import Sequence

DESKTOP = "C:\\Users\\djjch\\OneDrive\\Desktop"


def swap_backslash_for_fwdslash(path):
    return path.replace("\\", "/")


def append_slash_if_missing_in_path(path):
    if path[-1] != '/':
        path += '/'
    return path


def fix_path(path):
    path = swap_backslash_for_fwdslash(path)
    path = append_slash_if_missing_in_path(path)
    return path


def list_text_files_in_folder(pathname):
    # returns list naming every txt file in folder
    print('looking for text files in', pathname)
    return [filename for filename in sorted(os.listdir(pathname)) if filename.endswith('.txt')]

# todo returns list of filenames
def notes_exist_in_which_text_files(pathname, filelist, reserved_list):
    print("file list is", filelist)
    print("reserved files to avoid:", reserved_list)
    fileswithnotes = []
    for filename in filelist:
        if filename not in reserved_list:
            print("Checking", filename, "for notes...")
            with open(os.path.join(pathname, filename), 'r') as filetoread:
                fullfiletext = filetoread.read()
                if '->' in fullfiletext:
                    fileswithnotes.append(filename)
        else:
            print(filename, "found in reserved list, not checking")
    print("files containing notes:", ','.join(fileswithnotes))
    return fileswithnotes