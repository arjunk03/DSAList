a = [2,3,3,4,4,5,6,6,6,6,6,6,7,8,8,8,9,9,10]
a = [4]

i = j = 0
cnt = 1
for j in range(len(a)):
    if a[i] != a[j]:
        i+= 1
        a[i] = a[j]
        cnt += 1

print(a, cnt)