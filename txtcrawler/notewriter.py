from datetime import date

import notefinder
import notereader

def generate_datestamp():
    datestamp = date.today()
    return datestamp

# def append_to_ideas_file(paragraph, path="D:/repos/personalcode-master/personalcode/txtcrawler/textfiles/",
#                          filename='ideas.txt'):
#     path = notefinder.fix_path(path)
#     texttowrite = paragraph.replace("#ideas", "").replace("  ", "")
#     filetowrite = open(path + file, 'w')
#     filetowrite.write(generate_datestamp + "\n" + texttowrite)
#     filetowrite.close()

# def send to Google Keep
# there's no Keep API!

# def send to Todoist

# def send to quotes folder as separate file named for first hashtag after #quotes

# def send boilerplate text to Templates folder, if already file named corresponding to hashtag, append to file, else create file and append text
