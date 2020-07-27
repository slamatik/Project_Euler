def sieve(n):
    primes = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p] is True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    solution = []
    for p in range(2, n + 1):
        if primes[p]:
            solution.append(p)

    return solution


def rotate(n):
    n = str(n)
    for i in range(1, len(n)):
        temp = n[i:] + n[:i]
        if not prime_check(int(temp)):
            return False
    return True


def prime_check(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


count = 0
data = sieve(1000000)
for prime in data:
    if rotate(prime):
        count += 1

print(count)
