def sum_divisors(n):
    i = 2
    upper = n
    total = 1
    while i < upper:
        if n % i == 0:
            upper = n // i
            total += upper
            if upper != i:
                total += i
        i += 1
    return total


def is_abundant(n):
    return sum_divisors(n) > n


abundant = [i for i in range(12, 28123) if is_abundant(i)]
non_abundant = [i for i in range(28123)]

for n1 in range(len(abundant)):
    for n2 in range(n1, 28123):
        if abundant[n1] + abundant[n2] < 28123:
            non_abundant[abundant[n1] + abundant[n2]] = 0
        else:
            break

print(sum(non_abundant))
