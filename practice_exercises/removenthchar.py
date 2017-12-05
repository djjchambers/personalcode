def removenthchar(words, charnum):
    print(words[:charnum] + words[charnum+1:])
    
firstwords = "apple"
firstcharnum = 2
secondwords = "bingo"
secondcharnum = 4

removenthchar(firstwords, firstcharnum)
removenthchar(secondwords, secondcharnum)