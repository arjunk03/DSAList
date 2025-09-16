import math

def check_prime(val):
    for num in range(2, int(math.sqrt(val))+1):
        print(num)
        if val % num == 0:
            return False
        
    return True

data = 10
print(check_prime(data))


