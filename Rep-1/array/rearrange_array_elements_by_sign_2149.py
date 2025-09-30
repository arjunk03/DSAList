a = [5,10, -3, -1, -10, 6]

res = [0] * len(a)

pos = 0
neg = 1
for val in a:
    if val >= 0:   
        res[pos] = val
        pos += 2
    else:
        res[neg] = val
        neg += 2
print(res)