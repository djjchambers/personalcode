import os
from datetime import date

from notefinder import notes_exist_in_which_text_files, list_text_files_in_folder
from notereader import parse_notes

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
    # flag to determine what to call the file
    if infolder == False:
        print('infolder = False')
        filename = noteobject.maintag[1:] + '.txt'
        print('filename is maintag =', filename)
    else:
        subtags_nohash = [tag[1:] for tag in noteobject.subtags]
        filename = ('-'.join(subtags_nohash) + '.txt')
        print('filename is 2nd tag=', filename)
    # check for any subtags to append to note text
    if noteobject.subtags:
        texttoappend = noteobject.note + ''.join(noteobject.subtags)
    else:
        texttoappend = noteobject.note
        print('text to write =', texttoappend)
    # todo if file not found it doesn't create
    with open(os.path.join(pathname, filename), 'a+') as outfile:
        print('outfile to write to =', outfile)
        texttoappend_formatted = '-'*12 + '\n' + str(generate_datestamp()) + '\n' + texttoappend
        print('formatted text to write =', texttoappend_formatted)
        outfile.write(texttoappend_formatted)
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


# def write_to_google_drive(pathname, noteobject):
#     return "note written to google drive"

def send_to_todoist():
    pass

def publish_to_blog():
    pass

# todo def send to quotes file indexed by first hashtag after #quotes

# todo def send to Todoist

# todo def send boilerplate text to Templates folder, if already file named corresponding to hashtag, append to file, else create file and append text
#
# todo I need to figure out how to organise these modules and functions


actions = {
    '#ideas': [append_to_file, 'ideas'],
    '#quotes': [append_to_file, 'quotes'],
    '#todo': [send_to_todoist],
    '#boilerplate': [send_to_folder, 'templates'],
    '#care': [append_to_file, 'care'],
    '#planning': [append_to_file, 'planning'],
    '#pitch': [send_to_folder, 'pitch'],
    '#projects': [send_to_folder, 'projects'],
    '#blog': [publish_to_blog],
    '#journal': [append_to_file, 'journal'],
    '#remember': [append_to_file, 'remember']
}

files_not_to_read = ['ideas.txt', 'quotes.txt', 'care.txt', 'planning.txt', 'journal.txt', 'remember.txt']

read_path = 'C:/Users/djjch/OneDrive/Desktop/temp'
write_path = 'C:/Users/djjch/OneDrive/Documents/temp'

def main():
    # main program logic
    # find txt files, with tags, crawl through them
    # take each paragraph with tag into memory
    # delete from original file
    # decide where to send it
    # send it
    # if original file is empty, delete it

    list_of_text_files = list_text_files_in_folder(read_path)
    print('full list of text files in folder', list_of_text_files)
    files = notes_exist_in_which_text_files(read_path, list_of_text_files, files_not_to_read)
    print('/n'.join(files), 'found in', read_path, 'containing notes')
    for filename in files:
        infile = os.path.join(read_path, filename)
        print('Hey... reading -', infile)
        with open(infile, 'w+') as infiletext:
            print('text passed into writing function:', parse_notes(infiletext))
            for listitem in parse_notes(infiletext):
                print('first chunk of text=', listitem)
                maintag = listitem.maintag
                print('main tag =', maintag)
                if maintag in actions:
                    actions[maintag][0](actions[maintag][1], listitem)
                    print('calling', actions[maintag][0], 'with arguments', write_path, listitem)
                else:
                    print("invalid tag")
            # now call notecleaner to delete the notes from source file

if __name__ == "__main__":
    main()