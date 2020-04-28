import os
from datetime import date

import notefinder
import notereader
import notefiler


# ->ideas
# projects - for thing I've already started working on but aren't ready to show anyone, separate folder with text file
# pitch - for completed but not sold projects
# check for existing subtag#1 folder & (subtag#1)-notes.txt in it. If it exists, append note, if not, create folder/file
# boilerplate - folder with named subfolder/files
# learning - like projects but an area that I'm learning about ie programming/compsci. It needs to go somewhere.
# care - Google doc
# todo - Todoist API
# journal - append to txt file, encrypted on Google Drive
# planning - life admin stuff. Google doc
# remember - things that Kate has told me. Goes to ...
# comeback - a tag anywhere in the note that says keep this bubbling. Add to list somewhere?
# blog - a post that gets put into my microblog folder for next sync. (and then kicks off a git commit/push?)
# todo rearrange files/folder in hard drive to sync to Google Drive, just a Docs folder with all these files

def generate_datestamp():
    datestamp = date.today()
    return datestamp


def append_to_file(pathname, noteobject, infolder=False):
    if infolder == False:
        filename = noteobject.maintag[1:] + '.txt'
    else:
        subtags_nohash = [tag[1:] for tag in noteobject.subtags]
        filename = ('-'.join(subtags_nohash) + '.txt')
    # check for any subtags to append to note text
    if noteobject.subtags:
        texttoappend = noteobject.note + ''.join(noteobject.subtags)
    else:
        texttoappend = noteobject.note
    with open(os.path.join(pathname, filename), 'a') as filetowrite:
        texttoappend_formatted = '-'*12 + '\n' + str(generate_datestamp) + '\n' + texttoappend
        filetowrite.write(texttoappend_formatted)
    message = str('note written to ' + str(filename))
    return message


def send_to_folder(pathname, noteobject):
    # search for subtag[0]'s corresponding folder. Create if not found
    # create/open the file and append to it using append_to_file(subfolder=True)
    if not os.path.exists(pathname):
        os.mkdir(pathname)
    # inlining this following property feels wrong
    result = append_to_file(pathname, noteobject, infolder=True) + ' in folder ' + str(noteobject.maintag[1:])
    return result

def write_to_google_drive(pathname, noteobject):

    return "note written to google drive"

def send_to_todoist():
    pass

def publish_to_blog():
    pass

# todo def send to quotes file indexed by first hashtag after #quotes

# todo def send to Todoist

# todo def send boilerplate text to Templates folder, if already file named corresponding to hashtag, append to file, else create file and append text
#
# todo I don't understand json or Mock. I can't get todoist API to return anything. I need to figure out how to organise these modules and functions

# todo do I need to normalise this dict, ie make same amount of args for each key
actions = {
    '#ideas': [append_to_file, 'ideas'],
    '#quotes': [append_to_file, 'quotes'],
    '#todo': [send_to_todoist],
    '#boilerplate': [send_to_folder, 'boilerplate'],
    '#care': [write_to_google_drive, 'care'],
    '#planning': [write_to_google_drive, 'planning'],
    '#pitch': [send_to_folder, 'pitch'],
    '#projects': [send_to_folder, 'projects'],
    '#blog': [publish_to_blog],
    '#journal': [write_to_google_drive, 'journal'],
    '#remember': [write_to_google_drive, 'remember']
}

if __name__ == "__main__":
    # main program logic
    # find txt files, with tags, crawl through them
    # take each paragraph with tag into memory
    # delete from original file
    # decide where to send it
    # send it
    # if original file is empty, delete it
    ...