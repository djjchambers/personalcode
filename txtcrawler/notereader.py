import re
from dataclasses import dataclass, field


@dataclass
class Note:
    note: str
    maintag: str
    subtags: list = field(default_factory=list)
    comeback: bool = False


def parse_notes(input_file):
    L = []
    tagfixer_dict = {
        '#idea': '#ideas',
        '#project': '#projects',
        '#quote': '#quotes',
    }
    for item in input_file:
        # "->" is delimiter for beginning of notes
        # todo what if I forget the delimiter. Or what about a junk paragraph?
        # todo add a regex check for hashtags without a delimiter?
        fields = re.search(r'->(.*?)(#[a-zA-z0-9_\-]+.*)', item)
        if fields:
            tags = fields.group(2).split()
            if maintagtext in tagfixer_dict.keys():
                maintagtext = tagfixer_dict[maintagtext]
            note = Note(note=fields.group(1), maintag=maintagtext, subtags=tags[1:])
            L.append(note)
    return iter(L)