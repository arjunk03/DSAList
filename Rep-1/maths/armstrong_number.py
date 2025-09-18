import math
def check_armstrong(n):
    orig = n
    sm = 0
    no_of_digit = int(math.log10(n) + 1)
    #print(" no_of_digit",no_of_digit)
    while n > 0:
        dig = n % 10
        sm += dig ** no_of_digit
        n //= 10 
    
    return sm == orig 

n = 371
print(check_armstrong(n)) 


n = 1634
print(check_armstrong(n)) 

n = 1635
print(check_armstrong(n)) 