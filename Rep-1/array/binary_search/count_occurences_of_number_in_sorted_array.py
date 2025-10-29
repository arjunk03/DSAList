a = [3,4,5,5,6,7,7,7,8, 10,11, 11,12, 14, 16]

tgt = 7



def lower_bound(a, tgt):
    l = 0
    r = len(a) - 1
    lb = -1
    while l <= r:
        mid = l + (r-l)//2
        if a[mid] >= tgt:
            lb = mid
            r = mid -1
        else:
            l = mid + 1
    return lb

def upper_bound(a, tgt):
    l = 0
    r = len(a) - 1
    ub = -1
    while l <= r:
        mid = l + (r-l)//2
        if a[mid] > tgt:
            ub = mid
            r = mid - 1
        else:
            l = mid + 1
    return ub

start = lower_bound(a, tgt)
end = upper_bound(a, tgt) - 1

print(start, end)

print("total occurance: ", 0 if start == -1 else end-start+1)


