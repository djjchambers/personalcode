from sys import exit
import random

# define function to generate password, taking one parameter strength
def genpass(pass_strength):
	wordlist = ['apple', 'bear', 'coconut', 'deerstalker', 'euphonium', 'fresco', 'gramophone', 'hurdygurdy', 'inglenook', 'juniper', 'kettlebell', 'linoleum', 'martinet', 'nostrum', 'octothorpe', 'pumpernickel', 'quibble', 'rastafarian', 'senescent', 'trombone', 'uvula', 'vongole', 'wigwam', 'xylophone', 'yoghurt', 'zither']
	if pass_strength == 0:
		password = []
		for i in range(2):
			password.append(wordlist[random.randint(1, 26)])
		password = ''.join(password)
		return password
		
	else:
		pass_strength *= 8
		password = []
		while pass_strength > 0:
			passletter = random.randint(48, 122)
			password += chr(passletter)
			pass_strength -= 1
			
		password = ''.join(password)
		return password
	exit(0)
	
# ask for strength (0 to 2)
strength = int(input('Input strength of password (0: weak, 1: strong, 2: v strong): '))
if 0 > strength:
	strength = 0
elif strength > 2:
	strength = 2

print('Password is ', genpass(strength))