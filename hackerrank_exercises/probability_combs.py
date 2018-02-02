from itertools import combinations
a = input()
S = str(input().replace(' ', ''))
k = input()

# prob = number of tuples of length k with a in them, divided by no. of tuples.
n = list(combinations(S, int(k)))
count = 0
for element in n:
    if 'a' in element:
        count += 1
print('{0}'.format(count / len(n)))