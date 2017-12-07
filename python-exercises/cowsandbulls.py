import random

diglst = ''
guesses = won = 0

# generate random number
for soldigit in range(4):
	soldigit = str(random.randint(0, 9))
	diglst = diglst + soldigit
print(diglst)
	
while won == 0:
	# loop - get user input
	guess = str(input('Type a 4-digit number '))
	# update guess count
	guesses += 1
	cows = bulls = 0
	
	if len(guess) != 4:
		print('Not a 4-digit number!')
		break

	# test for success & break if got all numbers (while guess != solution)
	if (set(guess) == set(diglst)):
		print("Success in {}!".format(guesses))
		won = 1

	elif len(set(guess) & set(diglst)) >=1:
		bulls = len(set(guess) & set(diglst))
		
		for char in range(0,4):
			if str(guess[char]) == (diglst[char]):
				cows += 1
				
		bulls = bulls - cows
	
	print("{} cows, {} bulls. {} guesses".format(cows, bulls, guesses))