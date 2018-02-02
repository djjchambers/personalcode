import itertools

str = input()
s, k = str.split()
combs = []

for i in range(1, int(k) + 1):
    combs.append([sorted(list(comb)) for comb in itertools.combinations(s, i)])

for element in combs:
    for bit in sorted(element):
        print(''.join(bit))