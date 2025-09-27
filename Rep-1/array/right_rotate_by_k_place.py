# # Brute force solution
# def rotate(a, k):
#     if k % len(a) == 0:
#         return a
    
#     k = len(a) % k
#     n = len(a)
#     temp = a[n-1]
#     for ind in range(n-2, -1, -1):
#         a[ind+1] = a[ind]
    
#     a[0] = temp

# a = [3,23,4,56,5,3,4,6]
# k = 4

# print(a)
# for val in range(k):
#     rotate(a, 1)


# print(a)


# optimal

a = [3,23,4,56,5,3,4,6]
k = 4
def reverse(a, i , j):
    while i <= j:
        a[i], a[j] = a[j], a[i]
        i+= 1
        j-=1

n = len(a)
print(a, n , k) 
reverse(a , n-k, n-1 )
print(a)
reverse(a, 0, n-k-1)
print(a)
reverse(a, 0 , n-1)
print(a)