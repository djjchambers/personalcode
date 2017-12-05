def findlongestword(wordlist):
    
    length = 0
    
    for word in wordlist:
        if len(word) > length:
            length = len(word)
    
    print(length)
    
listofwords = ['bog', 'dog', 'catt', 'donkey', 'whale', 'antidisestablishmentarianism']

findlongestword(listofwords)