def check_palindrom(n):
    n_dup = n
    if n < 0: return False

    rev = 0
    while n > 0:
        dig = n % 10
        rev = (rev * 10) + dig
        n = int(n / 10)

    return rev == n_dup


a = 2346
print(check_palindrom(a))


a = 232
print(check_palindrom(a))


a = 53535
print(check_palindrom(a))