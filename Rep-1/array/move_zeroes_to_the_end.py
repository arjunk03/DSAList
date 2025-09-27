a = [5,7,0,6,0,5, 0,4,5,0,0,7,6,6,6]

i = 0
for ind in range(len(a)):
    print(i, ind, a[i], a[ind], a)
    if a[ind] != 0:
        a[i], a[ind] = a[ind], a[i]
        i += 1


print(a)
    