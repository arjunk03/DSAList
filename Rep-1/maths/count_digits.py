def count_digits(n):
    cnt = 0 
    while n >0 :
        dig = n % 10
        cnt += 1
        n = int(n / 10)
    
    return cnt

n = 1233425
print(count_digits(n))

def count_dig_bitwise(n):
    cnt = 0 
    while n > 0 :
        n = n >> 1
        cnt += 1
        
    return cnt

import math
def count_digits_log(n):
    return int(math.log10(n) + 1)

n = 123342556454545
# print(n.bit_count())
# print(n.bit_length())
# print(count_dig_bitwise(n))
print(count_digits_log(n))