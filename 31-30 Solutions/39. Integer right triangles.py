result = None
results_n_solution = 0
for p in range(2, 1001, 2):
    temp_n_solutions = 0
    for a in range(2, p // 3 + 1):
        if (p ** 2 - 2 * p * a) % (2 * p - 2 * a) == 0:
            temp_n_solutions += 1
    if temp_n_solutions > results_n_solution:
        result = p
        results_n_solution = temp_n_solutions

print(result)