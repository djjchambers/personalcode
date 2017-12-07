elements = [1, 1, 1, 1, 3, 4, 4, 5, 5, 6, 7, 8, 8, 8, 8]

def loopdupe(nums):
	numlist = []
	for item in nums:
		if item not in numlist:
			numlist.append(nums[item])
	return numlist
	
def setdupe(nums):
	numlist = sorted(set(nums))
	return numlist
	
print(loopdupe(elements))
print(setdupe(elements))