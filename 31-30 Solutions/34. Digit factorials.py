def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return factorial(n - 1) * n


results = []
for i in range(3, 50000):
    total = 0
    for digits in str(i):
        total += factorial(int(digits))
    if total == i:
        results.append(i)

print(sum(results))
