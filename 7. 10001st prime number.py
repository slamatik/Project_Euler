from math import sqrt


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


cnt, prime = 1, 1
while cnt < 10001:
    prime += 2
    if prime_check(prime):
        cnt += 1
print(prime)
