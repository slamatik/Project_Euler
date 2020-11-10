with open('p079_passcode.txt') as f:
    data = f.read().split('\n')

unique_numbers = (set(''.join(data)))
previous = {}
for pw in data:
    for n in range(2, 0, -1):
        current, points_to = pw[n], pw[n - 1]
        if current in previous:
            previous[current].append(points_to)
        else:
            previous[current] = [points_to]
    if pw[0] in previous:
        continue
    else:
        previous[pw[0]] = []


def find_empty(data):
    for key, val in data.items():
        if val == []:
            return key


def remove_value(data, num):
    del previous[num]
    for i in data.values():
        while num in i:
            i.remove(num)

soltuion = ''
while find_empty(previous):
    val = find_empty(previous)
    soltuion += val
    remove_value(previous, val)

print(soltuion)