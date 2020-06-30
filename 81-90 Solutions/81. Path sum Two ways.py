nums = []
with open("p081_matrix.txt") as f:
    for line in f:
        nums.append(list(map(int, line.strip().split(","))))


def find_min_path(data):
    n = len(data)
    table = [[0 for i in range(n)] for i in range(n)]
    table[0][0] = data[0][0]

    for x in range(1, n):
        table[0][x] = table[0][x - 1] + data[0][x]
    for y in range(1, n):
        table[y][0] = table[y - 1][0] + data[y][0]

    for y in range(1, n):
        for x in range(1, n):
            table[y][x] = min(table[y - 1][x], table[y][x - 1]) + data[y][x]

    return table[-1][-1]


print(find_min_path(nums))
