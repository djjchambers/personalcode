monthlyInterestRate = annualInterestRate / 12

for month in range(12):
	monthlyPayment = monthlyPaymentRate * balance
	balance -= monthlyPayment 
	balance += (balance * monthlyInterestRate)

print('Remaining balance:'.format(month + 1), (round(balance, 2)))