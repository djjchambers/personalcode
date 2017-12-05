numlist = []
item = 1

def evenprint(nums):
    for item in nums:
        if item % 2 == 0:
            numlist.append(nums[item])
    print(numlist)
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evenprint(numbers)