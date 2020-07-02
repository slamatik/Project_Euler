coins = [1, 2, 5, 10, 20, 50, 100, 200]
m = len(coins)
n = 200

table = [0 for i in range(n + 1)]
table[0] = 1


for i in range(0, m):
    for j in range(coins[i], n + 1):
        table[j] += table[j - coins[i]]

print(table)
print(table[n])
