a = [1,1,2,3,3,4,5,6,7,7,7]
b = [2,2,2,4,5,5,5,6,7,8,9,9,9]

res = []
i = j = 0
prev_val = float("inf")
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        if a[i] != prev_val:
            res.append(a[i])
            prev_val = a[i]
        i += 1
    else:
        if b[j] != prev_val:
            res.append(b[j])
            prev_val = b[j]
        j += 1

while i < len(a):
    if a[i]  != prev_val :
        res.append(a[i])
        prev_val = a[i] 
    i += 1

while j < len(b):
    if b[j]  != prev_val:
        res.append(b[j])
        prev_val = b[j]
    
    j += 1


print(res)
    
