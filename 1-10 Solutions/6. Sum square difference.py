def find_sum_squares(n):
    total = 0
    for i in range(n + 1):
        total += i ** 2
    return total


def find_square_of_sum(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total ** 2


print(find_square_of_sum(100) - find_sum_squares(100))
