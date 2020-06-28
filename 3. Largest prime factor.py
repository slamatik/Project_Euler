from math import sqrt


def find_largest_prime_factor(n):
    max_factor = 0

    while n % 2 == 0:
        max_factor = 2
        n /= 2

    for i in range(3, int(sqrt(n) + 1), 2):
        while n % i == 0:
            max_factor = i
            n /= i

    if n > 2:
        max_factor = n

    return max_factor


print(find_largest_prime_factor(600851475143))
