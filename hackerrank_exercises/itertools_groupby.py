from itertools import groupby
S = input()

print(*[(len(list(cgen)), int(c)) for c,cgen in groupby(S)])