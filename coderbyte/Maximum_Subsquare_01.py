def MaximalSquare(strArr): 
    
    R = len(strArr)
    C = len(strArr[0])
    sumArr = [[0 for k in range(C)] for l in range(R)]
    
    for i in range(1, R):
        for j in range(1, C):
            if int(strArr[i][j]) == 1:
                sumArr[i][j] = (min(int(sumArr[i][j-1]), int(sumArr[i-1][j-1]), int(sumArr[i-1][j])) + 1)
            else:
                sumArr[i][j] = 0
    L = [] 
    for a in sumArr:
        for b in a:
            L.append(b)
    return max(L) ** 2
    
# keep this function call here  
print(MaximalSquare(["10100", "10111", "11111", "10010"]))
print(MaximalSquare(["0111", "1111", "1111", "1111"]))
print(MaximalSquare(["101101", "111111", "011111", "111111", "001111", "011111"]))
print(MaximalSquare(["1111", "1111"]))
print(MaximalSquare(["1111", "1111", "1111"]))
