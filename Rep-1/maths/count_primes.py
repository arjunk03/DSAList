def count_prime(n):
    if n <= 1: return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for val in range(2, n):
        if is_prime[val]:
            for va2 in range(val*2, n, val):
                is_prime[va2] = False
    return len([val for val in is_prime if val])

n = 15
print(count_prime(n))