def sel_sort(arr):
    for ind1 in range(len(arr)):
        for j in range(ind1+1, len(arr)):
            if arr[ind1] > arr[j]:
                arr[ind1], arr[j] = arr[j], arr[ind1]

   

arr = [6,3,6,1,7,91,9,123,5]
sel_sort(arr)
print(arr)