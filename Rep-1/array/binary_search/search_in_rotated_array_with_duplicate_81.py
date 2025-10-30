a = [11, 12,13, 14, 14, 16,3,4,5,6,6,7,8,8, 9, 10,10]

tgt = 10

l = 0
r = len(a) -1
while l <= r:
    mid = l + (r-l)//2
    if a[mid] == tgt or a[l] == tgt or a[r] == tgt:
        print("found")
        break

    if a[l] == a[mid] == a[r]:
        l += 1
        r -= 1
        continue

    if a[mid] < a[r]:
        if a[mid] < tgt < a[r]:
            l = mid + 1
        else:
            r = mid - 1
    else:
        if a[l] < tgt < a[mid]:
            r = mid -1
        else:
            l = mid + 1
else:
    print("not found")
