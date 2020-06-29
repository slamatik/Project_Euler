def get_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append((n//i))
    return sum(divisors)


total = 0
for a in range(1, 10000):
    b = get_divisors(a)
    if 10000 > b != a and get_divisors(b) == a:
        total = total + a + b
print(total // 2)
