for a in range(500):
    for b in range(500):
        c = (a ** 2 + b ** 2) ** 0.5
        if a + b + c == 1000 and a < b < c:
            print(int(a * b * c))

