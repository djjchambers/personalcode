import string

def total(hi1, hi2):
    return hi1 + hi2
    
def score(word, f):
    L = []
    index = -1

    for letter in word:
        index += 1
#        print('letter', letter, 'index', index)
        if letter.isupper():
            offset = 64
        elif letter.islower():
            offset = 96
        alphscore = ord(letter)-offset
#        print('offset', offset, 'alphscore', alphscore)
#        print('calc',(alphscore)*index)
        L.append((alphscore)*index)
            
#    print('word scores', sorted(L))
    hi1 = sorted(L)[-1]
    hi2 = sorted(L)[-2]
#    print('highest', hi1, 'secondhighest', hi2)
    return f(hi1, hi2)
    
    
#print(score('aDd', total))