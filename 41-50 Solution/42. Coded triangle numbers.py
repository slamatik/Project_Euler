from string import ascii_uppercase

with open("p042_words.txt") as f:
    words = f.read().split(",")

triangle_numbers = [int(0.5 * n * (n + 1)) for n in range(1, 100)]

data = {}
for i, let in enumerate(ascii_uppercase, 1):
    data[let] = i


def word_value(word):
    value = 0
    for let in word:
        value += data[let]
    return value


cnt = 0
for word in words:
    if word_value(word.strip('"')) in triangle_numbers:
        cnt += 1

print(cnt)
