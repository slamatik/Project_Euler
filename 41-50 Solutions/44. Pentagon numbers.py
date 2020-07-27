pn = [n * (3 * n - 1) // 2 for n in range(1, 10000)]


def pent_check(n):
    disc = 1 + 4 * 3 * 2 * n
    if (1 + disc ** 0.5) % 6 == 0:
        return True
    return False


for j in pn:
    for k in pn:
        if pent_check(abs(j - k)) and pent_check(j + k):
            print(abs(j - k))
