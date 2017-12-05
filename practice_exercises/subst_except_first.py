words = input('String: ')

indx = 0

for char in words[1:]:
    if words[indx] == words[0]:
        words.replace(char, '$')
    indx += 1
    
print(words)