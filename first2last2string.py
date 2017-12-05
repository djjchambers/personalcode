userwords = input('string? ')

if len(userwords) < 2:
    print('String too short!')
    
print(userwords[0:2] + userwords[-2:])    