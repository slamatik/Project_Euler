def prime_check(n):
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


primes = []
for i in range(6, 1000000):
    if prime_check(i):
        primes.append(i)
    if sum(primes) > 1000000:
        primes.pop()
        break

print(sum(primes))
