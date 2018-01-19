s = 'abcdefghijklmnopqrstuvwxyz'
count = 0
tally = 0
L = []
res = ''
while count < (len(s) - 1):
    if s[count+1] >= s[count]:
        if count = len(s) - 1:
            tally += 1
            
        print(s[count+1], '>=', s[count])
        tally += 1
        print('tally', tally)
    else:
        print(s[count + 1], 'NOT <=', s[count])
        tally += 1
        print('tally', tally)
        if tally > len(res):
            print('New longest string found!')
            print(s, count, tally)
            res = s[count - (tally - 1):count + 1]
            print('Result so far', res)
        tally = 0
    print('count ', count)
    count += 1
    
print('Longest substring in alphabetical order is:', res)