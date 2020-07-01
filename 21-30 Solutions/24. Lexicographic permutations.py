from time import time

results = []


def permutations(data, st_id, end_id):
    if st_id == end_id:
        results.append("".join(data))
    else:
        for iter in range(st_id, end_id):
            data[st_id], data[iter] = data[iter], data[st_id]
            permutations(data, st_id + 1, end_id)
            data[st_id], data[iter] = data[iter], data[st_id]


string = "0123456789"
inp = list(string)
n = len(string)
start = time()
permutations(inp, 0, n)
results.sort()
print(results[999999])
print(time() - start)
