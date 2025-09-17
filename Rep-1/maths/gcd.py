def get_gcd(a, b):
    gcd = 1
    if a == b:
        return a
    if 0  in [a, b]:
        return max(a, b)
    for val in range(2, min(a,b)+1):
        if a % val == 0 and b % val  == 0:
            gcd = val

    return gcd

a = 4
b = 6
print(get_gcd(a,b))


a = 4
b = 0
print(get_gcd(a,b))


a = 10
b = 10
print(get_gcd(a,b))