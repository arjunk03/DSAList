def count_digits(n):
    """
    Counts the number of decimal digits in a given integer.
    Args:
        n (int): The integer whose digits are to be counted.
    Returns:
        int: The number of decimal digits in n.
    Note:
        - This function works for positive integers.
        - For n <= 0, the function will return 0.
    """
    """
    Counts the number of bits required to represent a given integer in binary.
    Args:
        n (int): The integer whose binary representation length is to be counted.
    Returns:
        int: The number of bits required to represent n.
    Note:
        - This function works for positive integers.
        - For n <= 0, the function will return 0.
        - This is similar to n.bit_length() in Python.
    """
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

n = 1233425
# print(n.bit_count())
# print(n.bit_length())
print(count_dig_bitwise(n))
