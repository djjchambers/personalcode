import string
d = {}
shift = 5
lowers = string.ascii_lowercase
uppers = string.ascii_uppercase
for letter in lowers:
    if ord(letter) + shift > 122:
        shifted = (ord(letter) - 26) + shift
    else:
        shifted = ord(letter) + shift
    d[letter] = chr(shifted)
for letter in uppers:
    if ord(letter) + shift > 90:
        shifted = (ord(letter) - 26) + shift
    else:
        shifted = ord(letter) + shift
    d[letter] = chr(shifted)
print(d)