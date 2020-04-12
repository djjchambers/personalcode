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


def list_text_files_in_folder(pathname: str) -> Sequence[str]:
    # returns list naming every txt file in folder
    return [filename for filename in sorted(os.listdir(pathname)) if filename.endswith('.txt')]


def hashtags_exist_in_which_of_5_text_files(pathname, filelist):
    filescontainingtags = []
    for filename in filelist:
        with open(os.path.join(pathname, filename), 'r') as filetoread:
            fullfiletext = filetoread.read()
            if '#' in fullfiletext:
                filescontainingtags.append(filename)
    return filescontainingtags


