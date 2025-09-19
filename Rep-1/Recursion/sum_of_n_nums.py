
def sum_of_n(sum_v, i, n):
    if i == n:
        return i
    return i + sum_of_n(sum_v,i+1, n)


sum_v = 0
a=5
print(sum_of_n(sum_v,1,a))



def sum_of_n(n):
    if n == 1:
        return 1
    return n + sum_of_n(n-1)


a=5
print(sum_of_n(a))




