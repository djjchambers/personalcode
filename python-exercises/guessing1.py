import random
inpwords = ""

while inpwords != "exit":
	guesses = []
	guess = ''
	guessnumber = 0
	a = random.randint(1, 10)
	while guess != a:
		guess = int(input('Guess the number (1-10): '))
		guessnumber += 1
			print('No input given!')
			break
		if guess > 10 or guess < 1:
			print('What are you, crazy?')
			break
		if guess not in guesses:
			if guess > a:
				guesses.append(guess)
				print('Lower!')
			elif guess < a:
				guesses.append(guess)
				print('Higher!')
		elif guess in guesses:
			print('You already guessed ', guess)
			print(guessnumber, ' guesses so far')			
				
	if guess == a:
		print('Bang on, me bucko!')
	else:
		print('Something went terribly wrong somewhere')
		
	inpwords = input('Type exit to quit> ')