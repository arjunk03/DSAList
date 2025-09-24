# def merge(arr, l , m, r):
#     print(arr, l,m,r)
#     while l <= m and m <= r:
#         print("enter")

#         print("idddd :", l , m, arr[l] , arr[m])
#         if arr[l] > arr[m]:
#             arr[l], arr[m] = arr[m], arr[l]
#             l += 1
#         else:
#             m += 1

       
def merge(left , right): 
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            res.append(right[j])
            j += 1
        else:
            res.append(left[i] ) 
            i += 1      

    res.extend(left[i:])
    res.extend(right[j:])

    return res
     

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    m = len(arr)//2

    # left_arr = merge_sort(arr, l, m)
    # right_arr = merge_sort(arr, m+1, r)
    left_arr = merge_sort(arr[:m])
    right_arr = merge_sort(arr[m:])

    final = merge(left_arr, right_arr)

    return final


arr = [6,3,6,1,7,91,9,123,5]
print(merge_sort(arr))
