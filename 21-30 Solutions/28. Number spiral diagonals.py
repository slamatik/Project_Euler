def spiral_diagonals(n):
    numbers = []
    i = 2
    num = 1
    while len(numbers) < (n * 2) - 1:
        numbers.append(num)
        num += i
        if len(numbers) % 4 == 0:
            i += 2
    return sum(numbers)


print(spiral_diagonals(1001))
