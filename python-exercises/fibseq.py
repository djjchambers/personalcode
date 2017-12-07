def fibsequence(num):
	L = []
	a, b = 1, 2
	i = 1
	while i < num:
		a, b = b, a + b
		L. append(a)
		i += 1
	print(L)