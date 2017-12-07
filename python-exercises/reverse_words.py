def reverse_words(sentence):
	return ' '.join(sentence.split()[::-1])

stuff = input('Type in a sentence: ')
print(reverse_words(stuff))