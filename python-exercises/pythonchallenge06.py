import re

target = 90052
TARGET_URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
cmt = ''

while True:
	file = open('C:\\Users\\dan\\Downloads\\channel\\' + str(target) + '.txt').read()
	found = re.findall('[0-9]+', file)
	if found:
		target = found[-1]
		print(target)
		cmt += file.getinfo('C:\\Users\\dan\\Downloads\\channel\\' + str(target) + '.txt').comment
	else:
		print(file)
print(cmt)