value = 100
nums = [i for i in range(1, value)]
m = len(nums)


def count(data, m, value):
    table = [0 for i in range(value + 1)]
    table[0] = 1

    for i in range(0, m):
        for j in range(data[i], value + 1):
            table[j] += table[j - data[i]]
    print(table)
    return table[value]


print(count(nums, m, value))
