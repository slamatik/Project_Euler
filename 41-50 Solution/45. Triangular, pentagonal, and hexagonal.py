from math import sqrt


def pent_check(n):
    solution = (1 + sqrt(1 + 4 * 3 * 2 * n))
    if solution % 6 == 0:
        return True


def hex_check(n):
    solution = (1 + sqrt(1 + 4 * 2 * n))
    if solution % 4 == 0:
        return True


found = False
while not found:
    for i in range(300, 1000000):
        triangle = i * (i + 1) // 2
        if pent_check(triangle) and hex_check(triangle):
            found = True
            print(triangle)
