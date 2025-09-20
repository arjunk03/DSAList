def bubb_sort(arr):
    for ind1 in range(len(arr)):
        for j in range(len(arr)-1-ind1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

   

arr = [6,3,6,1,7,91,9,123,5]
bubb_sort(arr)
print(arr)