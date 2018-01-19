print('Please think of a number between 0 and 100!')

hinum = 100
lonum = 0
correct = 0

while correct == 0:
    guess = int(hinum - ((hinum - lonum) / 2))
    print('Is your secret number {0}?'.format(guess))
    stuff = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if stuff == 'h':
        hinum = guess
        
    elif stuff == 'l':
        lonum = guess
        
    elif stuff == 'c':
        print('Game over. Your secret number was: {0}'.format(guess))
        break
        
    else:
        if len(stuff) != 1 or stuff not in 'hlc':
            print('Sorry, I did not understand your input.')