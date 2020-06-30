from string import ascii_uppercase

letters = ascii_uppercase
alphabet = {}
for i, let in enumerate(letters, 1):
    alphabet[let] = i


def get_letter_value(a):
    return alphabet[a]


def get_name_value(name):
    total = 0
    for i in name:
        total += get_letter_value(i)
    return total


with open('p022_names.txt') as f:
    names = f.read().split(",")
    names.sort()

total = 0
for en, name in enumerate(names, 1):
    total = total + get_name_value(name.strip('"')) * en

print(total)
