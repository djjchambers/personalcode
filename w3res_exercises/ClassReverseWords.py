from collections import deque
class Text():
    def __init__(self, words):
        self.words = words
    
    def get_reverse_words(self):
        L = deque()
        for word in self.words.split():
            L.appendleft(word)
        return ' '.join(L)
        
t = Text('agadoo doo doo push pineapple shake the tree')
print(t.get_reverse_words())