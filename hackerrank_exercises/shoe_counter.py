from collections import Counter
earnt = 0
n = input()
shoes = Counter(input().split())
ncust = int(input())
for i in range(ncust):
    size, price = input().split()
    if shoes[(size)] > 0:
        earnt += int(price)
        shoes[(size)] -= 1
        
print(earnt)