# # Recursive approach
# def get_gcd(a , b ):
#     if 0 in [a, b]:
#         return max(a,b)
    
#     if a > b:
#         return get_gcd(a % b, b)
#     else:
#         return get_gcd(a, b % a)

# Recursive approach 2
def get_gcd(a , b ):
    if b == 0: return a
    
    return get_gcd(b, a % b)
    

# # approach 2
# def get_gcd(a , b ):
   
#     while a > 0 and b > 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a

#     if 0 in [a, b]:
#         return max(a,b) 
    
a = 4
b = 6
print(get_gcd(a,b))


a = 4
b = 0
print(get_gcd(a,b))


a = 10
b = 10
print(get_gcd(a,b))



a = 6
b = 12
print(get_gcd(a,b))


