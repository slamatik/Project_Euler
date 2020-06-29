def count_paths(x, y):
    table = [1 for i in range(y)]
    for i in range(x - 1):
        for j in range(1, y):
            table[j] += table[j - 1]
    return table[y - 1]


print(count_paths(3, 3))
