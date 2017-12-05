words = input("Comma-separated list of words: ")

words = words.split(',')

words.sort()

for word in words:
    print(word)