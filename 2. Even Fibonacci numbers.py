memo = {}


def fibonacci(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if memo.get(x, 0) != 0:
        return memo[x]
    else:
        val = fibonacci(x - 1) + fibonacci(x - 2)
        memo[x] = val
        return val


solution = 0

for i in range(1, 35):
    val = fibonacci(i)
    if val % 2 == 0:
        solution += val

print(solution)
