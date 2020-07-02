results = []
p = 5
for number in range(1, 1000000):
    total = 0
    for digit in str(number):
        total += (int(digit) ** p)
    if total == number:
        results.append(number)

print(sum(results))
    