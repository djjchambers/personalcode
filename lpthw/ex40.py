# Make a class named Song that is-a object
class Song(object):
    
    # class Song has-a __init__ that takes self and lyrics parameters
    def __init__(self, lyrics):
        # from self, get the lyrics attribute and set it to the lyric parameter
        self.lyrics = lyrics
    
    # class Song has-a function named sing_me_a_song that takes self as a parameter
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
# set happy_bday to an instance of Song and pass the list of lyrics into it
happy_bday = Song(["Happy Birthday to you",
                       "I don't want to get sued",
                       "So I'll stop right here"])
    
bulls_on_parade = Song(["They rally round tha family",
                          "With pockets full of shells"])

frankenlyrics = bulls_on_parade.lyrics + ["braaaains"] + happy_bday.lyrics

frankensong = Song(frankenlyrics)
    
# from happy_bday, call the sing_me_a_song function
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

frankensong.sing_me_a_song()