# iteration
def fib(n):
    a, b = 0, 1

    cnt = 1
    while cnt < n:
        c = a + b
        a, b = b, c
        cnt += 1

    print("b", b)
    pass

print(fib(6))


# Recursion
def fib(n, a , b):
    if n == 1:
        return b
    
    return fib(n-1, b, a+b)

print(fib(6, 0,1))


# Recursion
def fib(n):
    if n <= 1:
        return n
          
    return fib(n-1) + fib(n-2)

print(fib(6))