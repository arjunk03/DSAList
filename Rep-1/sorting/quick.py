# def partition(arr,l, r):
#     if l > r:
#         return

#     i, j = l , r
#     pivot = arr[l]
    

#     while  i < j:
#         while arr[i] <= pivot and i <= r-1:
#             i += 1

#     while  i < j:
#         while arr[j] > pivot and j <= l+1:
#             j -= 1
 
#     if i < j:
#         arr[i], arr[j] = arr[j], arr[i]

#     arr[l] , arr[j] = arr[j], arr[l]
    
#     return  i

# def quick_sort(arr, l, r):
#     if l < r:
#         p_index = partition(arr, l , r)
#         quick_sort(arr, l , p_index-1)
#         quick_sort(arr, p_index+1, r)


# arr = [6,3,6,1,7,91,9,123,5,77,66]
# print(quick_sort(arr, 0 , len(arr)))


def quick_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot (here: the last element)
    pivot = arr[-1]
    
    # Partition step
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursively sort left and right partitions
    return quick_sort(left) + [pivot] + quick_sort(right)


# Example usage:
nums = [10, 7, 8, 9, 1, 5]
print("Unsorted:", nums)
print("Sorted:", quick_sort(nums))
