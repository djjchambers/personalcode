def isPalindrome(aString):
    hi = len(aString)
    lo = 0
    while len(aString) > 1:
        if aString[0] == aString[-1]:
            aString = aString[1:-1]
        else:
            return False
    return True
    
print(isPalindrome('madamimadam'))
print(isPalindrome('rotator'))
print(isPalindrome('bollocks'))