from math import log10

data = []
with open("p099_base_exp.txt") as f:
    for line in f:
        line = line.strip().split(",")
        data.append(line)

temp = int(data[0][1]) * log10(int(data[0][0]))
temp_index = 0
for i in range(1, len(data)):
    if int(data[i][1]) * log10(int(data[i][0])) > temp:
        temp = int(data[i][1]) * log10(int(data[i][0]))
        temp_index = i
    else:
        continue

print(temp_index + 1)
