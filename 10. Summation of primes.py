from math import sqrt
from time import time

def prime_check(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    limit = int(sqrt(n) + 1)

    for div in range(3, limit, 2):
        if n % div == 0:
            return False
    return True


total = 2

cnt, prime = 1, 1
while cnt < 200000:
    prime += 2
    if prime_check(prime):
        cnt += 1
        total += prime
    if prime > 2_000_000:
        break

print(total)
