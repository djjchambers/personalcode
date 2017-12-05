def upnlow(words):
    uppercount = 0
    lowercount = 1
    for char in words:
        if (words[char]).isupper():
            uppercount += 1
        elif (words[char]).islower():
            lowercount += 1

word = input("Type in a string: ")
upnlow(word)