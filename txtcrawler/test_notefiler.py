from freezegun import freeze_time

from notereader import Note
from notefiler import generate_datestamp, append_to_file, write_to_google_drive, send_to_folder


@freeze_time("25th December, 2019")
def test_generate_datestamp():
    datestamp = generate_datestamp().strftime('%Y-%m-%d')
    assert datestamp == '2019-12-25'

def test_append_to_file(tmpdir):
    # testing that write_to_ideas can take a note (the output of each iteration of notereader) in the form of note, maintag, subtags
    # and append it to ideas.txt in a given path
    note_01 = Note(note='a rubber bladder to contain air', maintag='#ideas', subtags=['#balloon', '#been_done'])
    assert append_to_file(tmpdir, note_01) == "note written to ideas.txt"
    note_02 = Note(note='learn the bongos', maintag='#bongos')
    assert append_to_file(tmpdir, note_02) == "note written to bongos.txt"

def test_send_to_folder(tmpdir):
    note_01 = Note(note='a rubber bladder to contain air', maintag='#project', subtags=['#balloon', '#been_done'])
    expected = "note written to balloon-been_done.txt in folder project"
    assert send_to_folder(tmpdir, note_01) == expected

def test_send_to_todoist(mocker):
    assert send_to_todoist()

def test_write_to_google_drive():
    noteobj = Note(note='a giant flying bladder filled with hydrogen', maintag='#research', subtags=['#zeppelin', '#oh_the_humanity'])
    if os.path.exists()
    assert write_to_google_drive(noteobj) == 'note written to google drive'