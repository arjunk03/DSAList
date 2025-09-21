def ins_sort(arr):
    for ind1 in range( len(arr)):
        j = ind1 - 1
        k = arr[ind1]
        while (arr[j] > k) and j>=0 :
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = k
       
   

arr = [6,3,6,1,7,91,9,123,5]
ins_sort(arr)
print(arr)