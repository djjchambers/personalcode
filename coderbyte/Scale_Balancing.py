import itertools
import re
def ScaleBalancing(currScale, weights): 

    # break it down.
    # select one weight, see if adding it to smallest weight works
    # select one weight from each, see if adding them in combo works
    print(currScale, weights)
    scales = (re.findall('\d+', currScale))
    weightList = list(map(int, re.findall('\d+', weights)))
    print(weightList)
    scaleA = int(scales[0])
    scaleB = int(scales[1])
    print(scaleA, scaleB)
    L = []
    
    # testing just one weight
    for weight in weightList:
        if scaleA + weight == scaleB or scaleA == scaleB + weight:
            L.append(weight)
            return sorted(L)
    
    for weightA, weightB in list(itertools.combinations(weightList, 2)):
        if scaleA + weightA + weightB == scaleB:
            L.extend([weightA, weightB])
        
        elif scaleA == scaleB + weightA + weightB or scaleA + weightA + weightB == scaleB:
            L.extend([weightA, weightB])
    
    return sorted(L)
    
# keep this function call here  
print(ScaleBalancing("[13, 4]", "[1, 2, 3, 6, 14]"))
















  