from time import time

memo = {}


def collatz_sequence(n):
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    else:
        if n % 2 == 0:
            temp = 1 + collatz_sequence(n // 2)
        else:
            temp = 1 + collatz_sequence(1 + 3 * n)
    memo[n] = temp
    return temp


start = time()
chain = 0
number = 0
for i in range(999_999, 1, -1):
    temp = collatz_sequence(i)
    if temp > chain:
        chain = temp
        number = i
print(chain)
print(number)
print(time() - start)
