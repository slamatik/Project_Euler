res = []
for a in range(100, 1000):
    for b in range(100, 1000):
        temp = a*b
        if str(temp) == str(temp)[::-1]:
            res.append(temp)
print(max(res))
