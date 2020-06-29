def count_sum_digits(n):
    num = str(n)
    total = 0
    for i in num:
        total += int(i)
    return total


print(count_sum_digits(2 ** 1000))
