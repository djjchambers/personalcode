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

def list_text_files_in_folder(path:str)->Sequence[str]:
    # returns list naming every txt file in folder
    return [filename for filename in sorted(os.listdir(path)) if filename.endswith('.txt')]
    
def list_text_files_containing_hashtags(list_of_filenames):
    count = 0
    for filename in list_of_filenames:
    with open()
    
def generate_datestamp():
    datestamp = date.today()
    return datestamp
    
def append_to_ideas_file(paragraph, path="D:/repos/personalcode-master/personalcode/txtcrawler/textfiles/", filename='ideas.txt'):
    path = fix_path(path)
    texttowrite = paragraph.replace("#ideas", "").replace("  ", "")
    filetowrite = open(path + file, 'w')
    filetowrite.write(generate_datestamp + "\n" + texttowrite)
    filetowrite.close()


# def send to Google Keep
# there's no Keep API!

# def send to Todoist

# def send to quotes folder as separate file named for first hashtag after #quotes

# def send boilerplate text to Templates folder, if already file named corresponding to hashtag, append to file, else create file and append text 


#def process_file_paragraph_by_paragraph(path, filename):
    # iterates through file by paragraph. If para contains hashtag, 
    #hashdict = {'#ideas': append_to_ideas_file,'#research': send_to_google_keep, '#quotes': append_to_quotes, '#todo': process_todo, '#boilerplate': process_boilerplate}
    
    #tmptext = []
    #filetowrite = open("tmp.txt", 'w')
    #filetoread = open(path + filename, 'r')
    #for paragraph in filetoread:
    #    for tag in hashdict.keys():
    #        if tag in paragraph:
    #            hashdict[tag](paragraph)
    #        else:
    #            tmptext.append(paragraph)
    #filetowrite.write('/n'.join(tmptext))
    #os.remove(filename)
    #os.rename(tmp.txt, filename)
    #filename.close()
    
if __name__ == "__main__":
    # program logic
    list_of_text_files = list_text_files_in_folder(DESKTOP)
    for file in list_of_text_files:
        process_file_paragraph_by_paragraph(DESKTOP, file)