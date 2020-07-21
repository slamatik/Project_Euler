with open("p067_triangle.txt") as f:
    data = [i.strip().split() for i in f.readlines()]
data = [[int(i) for i in lst] for lst in data]


def longest_slide_down(pyramid):
    for row in range(len(pyramid) - 2, -1, -1):
        for col in range(len(pyramid[row]) - 1, -1, -1):
            pyramid[row][col] += max(pyramid[row + 1][col], pyramid[row + 1][col + 1])
    return pyramid[0][0]


print(longest_slide_down(data))
