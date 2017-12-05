def checkpalindrome(word):
    if word == word[::-1]:
        print('Palindromic!')
    else:
        print('Fuck off!')
        
words = 'madam'
checkpalindrome(words)
words = 'rotator'
checkpalindrome(words)
words = 'gag'
checkpalindrome(words)
words = 'piss'
checkpalindrome(words)