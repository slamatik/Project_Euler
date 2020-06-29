data = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "onehundred",
    200: "twohundred",
    300: "threehundred",
    400: "fourhundred",
    500: "fivehundred",
    600: "sixhundred",
    700: "sevenhundred",
    800: "eighthundred",
    900: "ninehundred",
    1000: "onethousand",
}


def complete_data(n):
    if n in data:
        return data[n]
    if len(str(n)) == 2:
        temp = n - n % 10
        data[n] = data[int(str(temp))] + data[int(str(n % 10))]
        return data[n]
    if len(str(n)) == 3:
        temp = n % 100
        n -= temp
        return data[n] + "and" + complete_data(temp)


total = 0
for i in range(1, 1001):
    total += len(complete_data(i))
print(total)
