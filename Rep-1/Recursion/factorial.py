def fact(a):
    if a <= 1:
        return 1
    return a * fact(a-1)

n = 0
print(fact(n))