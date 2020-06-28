from math import sqrt


def prime_check(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    limit = int(sqrt(n)+1)

    for div in range(3, limit, 2):
        if n % div == 0:
            return False
    return True

res = []
cnt = 0
for i in range(1, 1000000):
    if prime_check(i):
        res.append(i)
        cnt += 1

print(res[10000])
