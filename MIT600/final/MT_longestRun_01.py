def longest_run(L):
    ctup = 1
    ctdn = 1
    sumup = L[0]
    sumdn = L[0]
    counter = 0
    d = {}
    for num in range(1, len(L)):
        if L[num] == L[num-1]:
            ctup += 1
            ctdn += 1
            if sumup == 0:
                sumup = L[num]
            elif sumup > 0:
                sumup += L[num]
            if sumdn == 0:
                sumdn = L[num]
            elif sumdn > 0:
                sumdn += L[num]
        if L[num] > L[num-1]:
            ctup += 1
            sumup += L[num]
            if ctdn > 1:
                if ctdn not in d:
                    d[ctdn] = sumdn
                ctdn = 1
                sumdn = L[num]
        if L[num] < L[num-1]:
            ctdn += 1
            sumdn += L[num]
            if ctup > 1:
                if ctup not in d:
                    d[ctup] = sumup
                ctup = 1
                sumup = L[num]
    if d:
        if ctdn > max(d):
            d[ctdn] = sumdn
        elif ctup > max(d):
            d[ctup] = sumup
    elif d == {}:
        if ctdn > ctup:
            d[ctdn] = sumdn
        else:
            d[ctup] = sumup
    print(d)

    return d[max(d)]
        
print(longest_run([1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))