def counting_summation(n):
    primes = sieve(n)
    m = len(primes)
    table = [[0 for i in range(n + 1)] for i in range(m)]

    for row in range(m):
        for col in range(1, n + 1):
            if col - primes[row] == 0:
                table[row][col] = table[row - 1][col] + 1
            else:
                table[row][col] = table[row - 1][col] + table[row][col - primes[row]]

    return table[-1][-1]


def sieve(n):
    nums = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if nums[p] is True:
            for i in range(p * p, n + 1, p):
                nums[i] = False
        p += 1

    solution = []
    for i in range(2, n + 1):
        if nums[i]:
            solution.append(i)

    return solution


i = 2
while True:
    temp = counting_summation(i)
    if temp > 5000:
        break
    i += 1
print(i)
