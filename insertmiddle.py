from sys import argv

script, bigstring, littlestring = argv

def insertintomiddle(words, inserter):
    
    middle = len(words) // 2

    words = (words[:middle] + inserter + words[middle:])
    print(words)

insertintomiddle(bigstring, littlestring)