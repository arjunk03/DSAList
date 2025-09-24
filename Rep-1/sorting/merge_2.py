def merge(arr, l , m, r):
    left = arr[l:m]
    right = arr[m:r]

    i, j = 0 , 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr[k] = right[j]
            j += 1
        else:
            arr[k] = left[i]
            i += 1
        k+= 1


    while i < len(left):
         arr[k] = left[i]
         k+= 1
         i += 1
    
    while j < len(right):
        arr[k] = right[j]
        j+= 1
        k+= 1


        

def merge_sort(arr, l , r):
    if r-l <= 1:
        return 
    
    m = (l+r)//2

    merge_sort(arr, l , m)
    merge_sort(arr, m, r)
    
    merge(arr, l , m , r)


arr = [6,3,6,1,7,91,9,123,5,77,66]
merge_sort(arr, 0 , len(arr))
print(arr)