def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def sum_digits(n):
    n = fact(n)
    total = 0
    for i in str(n):
        total += int(i)
    return total


print(sum_digits(100))
