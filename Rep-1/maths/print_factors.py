def get_factors(n):
    arr = []
    for val in range(1, n+1):
        print("val :", val)
        if n % val == 0:
            arr.append(val)

    return arr

# Better solution

def get_factors(n):
    arr = []
    for val in range(1, n//2+1):
        print("val :", val)
        if n % val == 0:
            arr.append(val)
    arr.append(n)
    return arr


# Best solution

def get_factors(n):
    arr = []
    for val in range(1, int(n **0.5)+1):
        print("val :", val)
        if n % val == 0:
            arr.append(val)
            div = int(n/val)
            if val != div:
               arr.append(div)

    return arr




a = 36
print(get_factors(a))
# a = 15
# print(get_factors(a))
# a = 7
# print(get_factors(a))