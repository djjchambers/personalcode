def pascaltrgl(num):
    
    pasclist = [1]
    for i in range(2, num):
        pasclist.append(pasclist[i-1] + pasclist[i])
        pasclist.append(1)
    
    print(pasclist)
    
number = 5
pascaltrgl(number)