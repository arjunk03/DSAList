a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

# brute force
res = [[0]* len(a) for _ in range(len(a))]

i = 0

while i < len(a):
    j = 0 
    while j < len(a):
        # res[j][i*-1-1] = a[i][j]
        res[j][(len(a)-1)-i] = a[i][j]
        j+= 1
    i+=1

print(res)


# optimal - First transpose the array and then reverse each row
i = 0

while i < len(a):
    j = i 
    while j < len(a):
        a[i][j], a[j][i] = a[j][i], a[i][j]
        j+= 1
    i+= 1


i = 0

while i < len(a):
    st, end = 0, len(a)-1
    while st <= end:
        a[i][st], a[i][end] = a[i][end] , a[i][st]
        st+=1
        end-=1
    i += 1

print(a)
