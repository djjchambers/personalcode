arr = [10,20,10,40,50,60,70]
target = 50

class Addpair():
	
	def get_pairs(L):
		pairs = []
		for i in range(len(L)):
			for j in range(i + 1, len(L)):
				pairs.append([int(L[i]), int(L[j])])
		return pairs
	
	def find_pairs(pairs, target):
		res = []
		for ctr in range(len(pairs)):
			if pairs[ctr][0] + pairs[ctr][1] == target:
				res.append([arr.index(pairs[ctr][0])])
		return(res)
				
add1 = Addpair.get_pairs(arr)
find1 = Addpair.find_pairs(add1, target)
print(find1)