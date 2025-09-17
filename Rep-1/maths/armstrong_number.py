def check_armstrong(n):
    orig = n
    sm = 0
    while n > 0:
        dig = n % 10
        sm += dig ** 3
        n //= 10 

    return sm == orig 

n = 371
print(check_armstrong(n)) 