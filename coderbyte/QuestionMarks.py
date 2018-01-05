import re
import string
def QuestionsMarks(str): 

	S = ''.join([i for i in str if not i.isalpha()])
	indices = [index for index, value in enumerate(S) if S[index].isdigit()]
	if indices != []:
		print(indices)
		c = 0
		while c < len(indices) - 1:
			print(int(S[indices[c]]) + int(S[indices[c+1]]))
			if (int(S[indices[c]]) + int(S[indices[c+1]])) == 10:
				chunk = S[indices[c]:indices[c+1]]
				print(chunk)
				if chunk.count('?') != 3:
					return False
			else:
				return False
			c += 1
	elif indices == []:
		return False
	return True
    
# keep this function call here  
print(QuestionsMarks("aaaaaaarrrrr??????"))
print(QuestionsMarks("mbbv???????????4??????ddsdsdcc9?"))
print(QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?a??5"))