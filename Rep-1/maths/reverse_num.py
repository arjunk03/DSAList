def get_rev(n):
    rev = 0
    while n > 0:
        dig = n % 10
        rev = (rev * 10) + dig
        n = int(n / 10)

    return rev


a = 2346
print(get_rev(a))

a = 5346
print(get_rev(a))


a = 1
print(get_rev(a))


a = 0
print(get_rev(a))


a = 23
print(get_rev(a))