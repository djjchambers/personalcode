numseq = input('list of numbers: ')
nums = numseq.split(',')
numlist = []

for num in nums:
    numlist.append(num)

numtuple = tuple(numlist)

print(numlist)
print(numtuple)