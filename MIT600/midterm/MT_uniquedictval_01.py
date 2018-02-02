def uniqueValues(aDict):
    dval = list(aDict.values())
    L = []
    for element in aDict:
        if dval.count(aDict[element]) == 1:
            L.append(element)
    return sorted(L)
    
print(uniqueValues({'a':3, 'b':2, 'c':2, 'd':1}))
print(uniqueValues({'a':1, 'b':1, 'c':1}))