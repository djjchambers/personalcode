import time
balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12

lopay = balance / 12
hipay = (balance * (1 + monthlyInterestRate * 12) / 12.0)
mid = lopay + ((hipay - lopay) / 2)

def bisect_search(balance, mid, lopay, hipay):
	currBal = balance
	for month in range(1, 13):
		currBal -= mid
		currBal += monthlyInterestRate * currBal
		print('month', month, 'guess', mid, 'bal', round(currBal, 2))

	if abs(currBal) < 0.01:
		print('Lowest Payment:', round(mid, 2))
		return
		
	elif currBal < -0.01:
		return bisect_search(balance, (lopay + ((hipay - lopay) / 2)), lopay, mid)
	
	elif currBal > 0.01:
		return bisect_search(balance, (lopay + ((hipay - lopay) / 2)), mid, hipay)

bisect_search(balance, mid, lopay, hipay)