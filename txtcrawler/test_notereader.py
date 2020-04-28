from io import StringIO

import pytest

from notereader import parse_notes


def test_read_simple_note():
    notes = "->sheep made of balloons befriends ardently religious anteater #ideas"
    # load into stringbuffer
    parsed_notes = parse_notes(StringIO(notes))
    note01 = next(parsed_notes)
    assert note01.note == "sheep made of balloons befriends ardently religious anteater "
    assert note01.maintag == "#ideas"
    assert note01.subtags == []


def test_read_simple_note_2():
    notes = ["->sheep made of balloons befriends ardently religious anteater #ideas", "->gloves made of sponge pudding #ideas #gloves #sponge-pudding"]
    parsed_notes = parse_notes(StringIO("\n".join(notes)))
    next(parsed_notes)
    note02 = next(parsed_notes)
    assert note02.note == "gloves made of sponge pudding "
    assert note02.maintag == "#ideas"
    assert note02.subtags == ["#gloves", "#sponge-pudding"]

def test_replace_idea_with_ideas():
    notes = '->sheep made of balloons befriends ardently religious anteater #idea'
    parsed_notes = parse_notes(StringIO(notes))
    note01 = next(parsed_notes)
    assert note01.maintag == '#ideas'

def test_read_non_tag_note():
    notes = ["->crazy horse is in the watering can #poem", "->blah blah no tag to see here"]
    parsed_notes = parse_notes(StringIO("\n".join(notes)))
    assert len(list(parsed_notes)) == 1

def test_return_number_of_notes():
    # todo - move this functionality into the actual function, rather than just test function. It's useful to have passed in to main program
    # todo - as a log/output response from running the script.
    countdict = {}
    notes = ["->crazy horse is in the watering can #poem", "an incorrectly formatted idea #ideas", "a junk paragraph", "->another silly idea #ideas"]
    parsed_notes = parse_notes(StringIO("\n".join(notes)))
    for note in list(parsed_notes):
        if note.maintag in countdict.keys():
            countdict[note.maintag] += 1
        else:
            countdict[note.maintag] = 1
    assert countdict == {
        '#poem': 1,
        '#ideas': 1
    }