import random
def CorrectPath(str): 
    dir = {'l':(-1,0), 'r':(1,0), 'u':(0,-1), 'd':(0,1)}
    tried = []
    invalid = ['lr', 'rl', 'ud', 'du']
    arrived = False
    while arrived == False:
        L = []
        # fill wildcards ('?') in string with guesses
        for char in str:
            if char != '?':
                L.append(char)
            elif char == '?':
                L.append(random.choice('lrud'))
        # toss out strings involving invalid chunks
        for chunk in invalid:
            if chunk in ''.join(L):
                break
        # winnow out strings already tried
        if L not in tried:
            print(''.join(L))
            tried.append(L)
        else:
            break

        coord_x = 0
        coord_y = 0
            
        # walk through try
        for i in L:
            print(i)
            
            coord_x += dir[i][0]
            coord_y += dir[i][1]
            print(coord_x, coord_y)
            # make sure to keep within grid
            if coord_x < 0 or coord_x > 4:
                arrived = False
                break
            if coord_y < 0 or coord_y > 4:
                arrived = False
                break
        if coord_x == 4 and coord_y == 4:
            arrived == True
            break
        else:
            arrived = False

    return(''.join(L))
    
    
# keep this function call here  
print(CorrectPath("???rrurdr?"))
print(CorrectPath("drdr??rrddd?"))