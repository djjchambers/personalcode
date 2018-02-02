def longest_run(L):

    longestup = []
    longestdown = []
    longest = []
    print('FIRST LOOP - UP')
    up = []
    down = []
    for i in range(1, len(L)):
        
        print('-'*12)
        if L[i] >= L[i-1]:
            if i == 1:
                up.append(L[i-1])
            print(L[i], '>', L[i-1])
            up.append(L[i])
            print('up', up)
            if i == len(L):
                print('end of list')
                up.append(L[i])
                print('up', up)
    print('COMPARING TO LONGEST')
    if len(up) > len(longest):
        print('longer up than longest')
        longestup = up
        print('longestup', longestup)
    
    print('SECOND LOOP - DOWN')
    for j in range(1, len(L)):
        
        print('-'*12)
        if L[j] <= L[j-1]:
            if j == 1:
                down.append(L[j-1])
            print(L[j], '<', L[j-1])
            down.append(L[j])
            print('down', down)
#            if j == len(L):
#                print('end of list')
#                down.append(L[j])
#                print('down', down)
    print('COMPARING TO LONGEST')
    if len(down) > len(longest):
        print('longer down than longest')
        longestdown = down
        print('longestdown', longestdown)
    
    print('FINISHED - COMPARING UP & DOWN')
    if len(longestup) > len(longestdown):
        print('up longer than down')
        longest = longestup
    else:
        print('down longer than up')
        longest = longestdown
    return sum(longest)
    
print(longest_run([1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(longest_run([100, 200, 300, -100, -200, -1500, -5000]))
print(longest_run([1, 2, 3, 2, -1, -10]))