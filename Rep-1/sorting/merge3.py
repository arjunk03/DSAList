def merge(left, right):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
           res.append(right[j])
           j += 1
        else:
            res.append(left[i])
            i += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2

    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    return merge(left_arr, right_arr)



arr = [6,3,6,1,7,91,9,123,5]
print(merge_sort(arr))