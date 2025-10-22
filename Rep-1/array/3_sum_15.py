a = [-1,0,1,2,-1,-4]

res = set()
# brute force
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            if a[i] + a[j] + a[k] == 0:
                b = [a[i] , a[j] , a[k]]
                b.sort()
                res.add(tuple(b))
print(res)


# better 
res = set()
# brute force
for i in range(len(a)):
    rem = set()
    for j in range(i+1, len(a)):
        third = -(a[i] + a[j])
        if third  in rem:
            b = [a[i], a[j], third]
            b.sort()
            res.add(tuple(b))
        rem.add(a[j])

print(res)


# optimal
a.sort()
res = set()
for i in range(len(a)-2):
    l, r = i+1, len(a) -1
    while l < r:
        tmp = a[i] + a[l] + a[r]
        if tmp == 0:
            res.add((a[i] ,  a[l] , a[r]))
            l += 1
            r -= 1
        elif tmp > 0:
            r -=1
        else:
            l += 1

print(res)