def bin_pal(n):
    number = bin(n)[2:]
    return number == number[::-1]


def number_pal(n):
    number = str(n)
    return number == number[::-1]


total = 0
for i in range(1, 1_000_000):
    if bin_pal(i) and number_pal(i):
        total += i

print(total)
