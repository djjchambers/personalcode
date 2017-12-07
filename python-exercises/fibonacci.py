num = int(input('how many fibs? '))

def fibfunk(fibnum):
	a = 0
	startnum = 1
	for i in range(1, fibnum):
		print(a + startnum)
		a, startnum  = startnum, a + startnum

fibfunk(num)