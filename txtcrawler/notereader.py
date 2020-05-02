import re
from dataclasses import dataclass, field


@dataclass
class Note:
    note: str
    maintag: str
    subtags: list = field(default_factory=list)
    comeback: bool = False

# this function doesn't keep count of how many notes there are
# or where we are in the file, so writing to temp file isn't poss
def parse_notes(input_file):
    print('input file =', input_file)
    L = []
    tagfixer_dict = {
        '#idea': '#ideas',
        '#project': '#projects',
        '#quote': '#quotes',
    }
    # todo what if I forget the delimiter. Or what about a junk paragraph?
    # todo add a regex check for hashtags without a delimiter?
    # todo ValueError: I/O operation on closed file here. input_file must be closed somewhere,
    # todo how to iterate over input_file for all the notes?
    for item in input_file:
        print('individual item =', item)
        # todo fix this regex with end of word after last tag
        fields = re.search(r'->(.*?)(#[a-zA-z0-9_\-]+.*)', item)
        if fields:
            print('regex fields =', fields)
            tags = fields.group(2).split()
            maintagtext = tags[0]
            note = Note(note=fields.group(1), maintag=maintagtext, subtags=tags[1:])
            if note.maintag in tagfixer_dict.keys():
                note.maintag = tagfixer_dict[note.maintag]
            L.append(note)

    return L