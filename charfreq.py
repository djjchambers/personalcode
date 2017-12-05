charfreq = {}

stuff = input('Type in a string: ')

for char in stuff:
    if char in charfreq:
        charfreq[char] += 1
    else:
        charfreq[char] = 1

print(charfreq)