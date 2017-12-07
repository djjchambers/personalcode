
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 'Michael']
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'Michael', 13]

if len(a) >= len(b):
    print([item for item in a if item in b])
elif len(a) < len(b):
    print([item for item in b if item in a])
