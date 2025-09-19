def rev(arr, l, r):
    if l == r:
        return
    
    arr[l], arr[r] = arr[r], arr[l]
    rev(arr, l+1, r-1)



ar = [1,2,3,4,5]
rev(ar, 0, len(ar)-1)
print(ar)


ar = [1,2,3,4,5, 6,7]
rev(ar, 2, 4)
print(ar)
