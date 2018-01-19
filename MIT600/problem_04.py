def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    L = []
    if aDict == {}:
        return None
    else:
        for element in aDict.keys():
            print(element)
            if len(aDict[element]) > len(L):
                L = aDict[element]
    return L

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

biggest(animals)