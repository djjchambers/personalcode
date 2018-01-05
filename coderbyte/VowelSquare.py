def VowelSquare(terms): 
    strArr = [x for x in terms]
    vowels = 'aeiou'
    R = len(strArr)
    C = len(strArr[0])
	
    L = []
	
    for i in range(R - 1):
        for j in range(C - 1):
            if strArr[i][j] in vowels and strArr[i+1][j] in vowels and strArr[i+1][j+1] in vowels and strArr[i][j+1] in vowels:
                L.append((i, j))
    if L == []:
        return 'not found'
    else:
        res = (sorted(L, key=lambda x: x[1]))
        return ''.join(str(res[0][0])+'-'+(str(res[0][1])))
		
# keep this function call here  
print(VowelSquare(("aqrst", "ukaei", "ffooo")))
