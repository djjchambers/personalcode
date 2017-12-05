import string

def wordoccurs(sentence):
    
    n = 0
    counts = dict()
    sentencewithoutpunct = ""
    
    for i in sentence:
        if sentence[n] = "." or ",":
            sentencewithoutpunct = (sentence[:n] + sentence[n+1:])
        n += 1
    
    words = sentencewithoutpunct.split(' ')
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
            
    print(counts)
    
wordstosearch = 'Froggy went a courtin he did ride, uh-huh. Froggy went a courtin he did ride uh-huh. Froggy went a courtin he did ride, sword and pistol by his side, uh-huh.'

wordoccurs(wordstosearch)