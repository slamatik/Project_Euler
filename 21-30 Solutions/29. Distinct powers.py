def combinations(low, high):
    numbers = []
    for a in range(low, high + 1):
        for b in range(low, high + 1):
            numbers.append(a ** b)
    numbers = set(numbers)
    return len(numbers)


print(combinations(2, 101))
