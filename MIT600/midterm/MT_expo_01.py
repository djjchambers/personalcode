def closest_power(base, num):
    n = 0
    expo = 0
    while expo <= num:
        expo = base**n
        n += 1
    grt = abs(num - expo)
    lsr = abs(num - (base**(n-2)))
    if lsr <= grt:
        return n-2
    elif lsr > grt:
        return n-1