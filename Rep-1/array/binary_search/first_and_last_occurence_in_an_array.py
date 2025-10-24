a = [3,4,5,5,6,7,7,7,8, 10,11, 11,12, 14, 16]

tgt = 7

l = 0
r = len(a) - 1
start = end = -1
while l <= r:
    mid = l + (r-l)//2
    if a[mid] == tgt:
        
        st = mid
        while a[st] == tgt and st >=0:
            st -= 1

        start = 0 if st < 0 else st + 1

        st = mid
        while a[st] == tgt and st <= len(a):
            st += 1
        
        end = 0 if st > len(a) else st - 1

        break

    elif a[mid] > tgt:

        r = mid - 1
    else:
        l = mid + 1

print(start, end)


# optimal

l = 0
r = len(a) - 1