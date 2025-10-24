a = [3,4,5,5,6,7,7,7,8, 10,11,12, 14, 16]

tgt = 15  

# Brute force
floor = -1
ceil = float("inf")

for val in a:
    # print("floor :", val , floor < val < tgt)
    # print("ceil :", val , ceil > val > tgt)
    if floor < val < tgt:
        floor = val
    elif ceil > val > tgt:
        ceil = val
    elif val == tgt:
        ceil = floor = val

print(floor, ceil)


#better
a = [3,4,5,5,6,7,7,7,8, 10,11,12, 14, 16]

tgt = 15  
floor = -1
ceil = float("inf")
l = 0
r = len(a) - 1 
while l <= r:
    mid = l + (r-l)//2
    if a[mid] == tgt:
        ceil = floor = a[mid]
        break 
    elif a[mid] > tgt:
        ceil = a[mid]
        r = mid - 1
    else:
        floor = a[mid]
        l = mid + 1

print(floor, ceil)