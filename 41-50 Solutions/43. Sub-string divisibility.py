from itertools import permutations


def delete_rep(num):
    num = str(num)
    for i in num:
        if num.count(i) > 1:
            return True
    return False


div11 = [str(i) for i in range(500, 601) if i % 11 == 0 and not delete_rep(i)]
div13 = [str(i) for i in range(1, 1001) if i % 13 == 0 and not delete_rep(i)]
div17 = [str(i) for i in range(1, 1001) if i % 17 == 0 and not delete_rep(i)]


def check_by_two(d2, d3, d4):
    if d2 == '0':
        d2 = ''
    return int(d2 + d3 + d4) % 2 == 0


def check_by_three(d3, d4, d5):
    if d3 == '0':
        d3 = ''
    return int(d3 + d4 + d5) % 3 == 0


def check_by_five(d4, d5, d6):
    if d4 == '0':
        d4 = ''
    return int(d4 + d5 + d6) % 5 == 0


def check_by_seven(d5, d6, d7):
    if d5 == '0':
        d5 = ''
    return int(d5 + d6 + d7) % 7 == 0


solution = []


def new_func(nums):
    remaining_nums = [str(i) for i in range(10) if str(i) not in nums]
    # print(remaining_nums)
    for i in permutations(remaining_nums):
        d1 = i[0]
        d2 = i[1]
        d3 = i[2]
        d4 = i[3]
        d5 = i[4]
        d6 = '5'
        if check_by_two(d2, d3, d4) and \
                check_by_three(d3, d4, d5) and \
                check_by_five(d4, d5, d6) and \
                check_by_seven(d5, d6, d7):
            solution.append(int(''.join([d1, d2, d3, d4, d5] + nums)))


for n11 in div11:
    current_data = {'d6': 5}
    d7, d8 = n11[-2], n11[-1]
    for n13 in div13:
        if n13.startswith(d7 + d8):
            d9 = n13[-1]
            for n17 in div17:
                if n17.startswith(d8 + d9):
                    d10 = n17[-1]
                    data = [d7, d8, d9, d10]
                    if len(set(data)) == 4:
                        if '0' in data and '5' in data:
                            break
                        current_data['d7'] = int(d7)
                        current_data['d8'] = int(d8)
                        current_data['d9'] = int(d9)
                        current_data['d10'] = int(d10)
                        data.insert(0, '5')
                        new_func(data)

print(sum(solution))