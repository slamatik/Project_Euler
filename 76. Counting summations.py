target = 100
ns = range(1, target)
ways = [1] + [0]*target

for n in ns:
    for i in range(n, target+1):
        ways[i] += ways[i-n]

print(ways[target])