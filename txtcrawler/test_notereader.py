from io import StringIO

import pytest

from notereader import parse_notes


def test_read_simple_note():
    notes = "sheep made of balloons befriends ardently religious anteater #ideas"
    # assign first iteration of notes as StringIO object to parsed_notes
    parsed_notes = parse_notes(StringIO(notes))
    # error - str expected in re-findall (in parse_notes) not list
    note01 = next(parsed_notes)
    assert note01.note == "sheep made of balloons befriends ardently religious anteater "
    assert note01.maintag == {"#ideas"}

def test_read_simple_note_2():
    notes = ["sheep made of balloons befriends ardently religious anteater #ideas", "gloves made of sponge pudding #ideas #gloves #sponge-pudding"]
    parsed_notes = parse_notes(StringIO("\n".join(notes)))
    next(parsed_notes)
    note02 = next(parsed_notes)
    assert note02.note == "gloves made of sponge pudding "
    assert note02.maintag == "#ideas"