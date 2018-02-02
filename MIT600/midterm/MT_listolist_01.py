#[[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into #[1,'a','cat',2,3,'dog',4,5] (order matters)

# iterate over list, for element in list
# check if element is list
# if so, iterate over it. If not, append it to master list
# how do you stop strings from being iterated over? 'type' command

def flatten(L):
    master = []
    for element in L:
        if not isinstance(element, list):
            master.append(element)
        else:
            master.extend(flatten(element))
    return master
    
    
print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))
master = []
print(flatten([[1, 2, 3], [[1, 2], ['a', 1, ['banana', 'apple'], 'b']]]))
master = []
print(flatten([]))
master = []
print(flatten(['arse', 'arse', 11, 1, {'a':1}, 1, ['cock and balls'], ['arse', 0]]))
master = []
print(flatten([[[[[[[[]]]]]]]]))