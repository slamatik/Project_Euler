from time import time

st = time()


def sieve(n):
    primes = [True for i in range(n + 1)]
    p = 2
    while p ** 2 <= n:
        if primes[p] is True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    sol = []
    for num in range(2, n + 1):
        if primes[num]:
            sol.append(num)
    return sol


def bi_search(data, n):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == n:
            return True
        elif data[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return False


def truncatable(n):
    #  L->R check
    cnt = 0
    i = 10
    while cnt < len(str(n)):
        if not bi_search(primes, n % i):
            return False
        # if n % i not in primes:
        #     return False
        i *= 10
        cnt += 1

    #  R->L check
    cnt = 0
    i = 1
    while cnt < len(str(n)):
        if not bi_search(primes, n // i):
            return False
        # if n // i not in primes:
        #     return False
        i *= 10
        cnt += 1
    return True


primes = sieve(1000000)

solution = []
for i in primes[5:]:
    if truncatable(i):
        solution.append(i)

print(sum(solution))
print(time() - st)
