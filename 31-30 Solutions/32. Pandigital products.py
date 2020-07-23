from time import time

start = time()


def check_pandigital(n):
    if sorted(n) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True


solution = []

for i in range(9):
    for j in range(999, 9999):
        number = str(i * j) + str(i) + str(j)
        if len(number) == 9 and check_pandigital(number):
            solution.append(i * j)
        elif len(number) > 9:
            break

for i in range(9, 99):
    for j in range(99, 999):
        number = str(i * j) + str(i) + str(j)
        if len(number) == 9 and check_pandigital(number):
            solution.append(i * j)
        elif len(number) > 9:
            break

print(sum(set(solution)))
print(time() - start)
