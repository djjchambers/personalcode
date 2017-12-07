import random
elements = ('Rock', 'Paper', 'Scissors')
# create matrix of game scores
victorylogic = ([0,1,-1],
				[-1,0,1],
				[1,-1,0])

# define score variables
p_one_score = 0
p_two_score = 0

# couldn't think of a more succinct way of doing this
while (p_one_score < 2) and (p_two_score < 2):
	# get input from player and computer and assign them to 2 vars
	play1 = int(input('Rock (1), Paper(2) or Scissors(3)?> '))
	play2 = random.randint(1, 3)
	
	# print the two choices (in string form)
	print(elements[play1 - 1])
	print('You chose ' + elements[play1 - 1])
	print('Computer chose ' + elements[play2 - 1])
	
	# game logic. Referring to the logic matrix, if it's -1 player1 (y) wins, if it's 1, computer (x) wins. Else it's a draw
	if (victorylogic[play1 - 1][play2 - 1]) == 1:
		p_two_score += 1
	elif (victorylogic[play1 - 1][play2 - 1]) == -1:
		p_one_score += 1
		
	print("Your score: ", p_one_score)
	print("Comp score: ", p_two_score)

# check if victory state has been reached, if not repeat round
if p_one_score >= 2:
	print("Player won!")
elif p_two_score >= 2:
	print("Computer won!")
else:
	print("Something fucked up!")