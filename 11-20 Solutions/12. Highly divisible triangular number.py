from math import sqrt


def triangular_number(n):
    number = 0
    for i in range(1, n+1):
        number += i
    return number


def prime_factorization(n):
    divisors = []

    while n % 2 == 0:
        divisors.append(2)
        n //= 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            divisors.append(i)
            n //= i

    if n > 2:
        divisors.append(n)

    return divisors


def count_divisors(n):
    array = prime_factorization(n)
    results = {}
    for i in array:
        results[i] = array.count(i)

    number = 1
    for i in results:
        number *= results[i] + 1

    return number



n = 1
while count_divisors(triangular_number(n)) < 500:
    n += 1
print(triangular_number(n))
