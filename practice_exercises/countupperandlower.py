# get input and assign it to var words
words = str(input('Input some text: '))

# define function countupperlower which take params self, sentence
def countupperlower(sentence):
    # assign local vars character, countupper, countlower and countneither
    character = 0
    countupper = 0
    countlower = 0
    countneither = 0
    # iterate through the sentence and increment the values of countupper, countlower in turn, defaulting to countneither
    while character < (len(sentence)):
        print(character)
        print(sentence[character])
        if sentence[character].isupper():
            countupper += 1
            print("countupper: ", countupper)
        elif sentence[character].islower():
            countlower += 1
            print("countlower: ", countlower)
        else:
            countneither += 1
            print("countneither: ", countneither)
        character += 1
    print('Countlower= ', countlower, 'Countupper= ', countupper, 'Countneither= ', countneither)

countupperlower(words)