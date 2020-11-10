def sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] is True:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    prime[0] = False
    prime[1] = False

    solution = []

    for i in range(1000, n + 1):
        if prime[i]:
            solution.append(i)

    return solution


data = sieve(10000)
n = len(data) - 1
for x in range(n):
    for y in range(x + 1, n):
        if sorted(str(data[x])) != sorted(str(data[y])):
            continue
        yx = data[y] - data[x]
        for z in range(y + 1, n):
            zy = data[z] - data[y]
            if yx != zy or sorted(str(data[x])) != sorted(str(data[z])):
                continue
            else:
                print(str(data[x]) + str(data[y]) + str(data[z]))
