a = [3,23,4,56,5,3,4,6]

def reverse(a, i , j):
    while i <= j:
        a[i], a[j] = a[j], a[i]
        i+= 1
        j-=1

reverse(a, 2,4)

print(a)