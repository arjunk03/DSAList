a = [3,23,4,56,5,3,4,6]

a[:] = a[-1:] + a[:-1]
print(a)

# solution 2
a = [3,23,4,56,5,3,4,6]
n=len(a)
temp = a[n-1]
for ind in range(n-2, -1, -1):
    a[ind+1] = a[ind]
a[0] = temp
print(a)
