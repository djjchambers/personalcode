from itertools import combinations_with_replacement as combrep

S, k = input().split()
L = []
for item in [sorted(chunk) for chunk in combrep(S, int(k))]:
    L.append(item)
    
for element in sorted(L):
    print(''.join(element))