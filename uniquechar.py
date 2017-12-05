newlist = []

def uniquechars(nums):
    for num in nums:
        if num not in(newlist):
            newlist.append(num)
    print(newlist)

numberlist = input('Type comma separated list of integers: ').split(',')
uniquechars(numberlist)