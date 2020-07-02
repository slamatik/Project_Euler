from time import time

# my
# def fibonacci(n):
#     first, second = 1, 1
#     for i in range(1, n):
#         first, second = second, first + second
#     return first
#
#
# start = time()
# for i in range(1, 5000):
#     if len(str(fibonacci(i))) == 1000:
#         print(i)
#         break
# print(time()-start)


# a bit better one
# def len_fib(n):
#     first, second = 1, 1
#     i = 1
#     while len(str(first)) != n:
#         first, second = second, first + second
#         i += 1
#     return i

# a lot better one
from math import log10

start = time()

i = 2
a = [1, 1]

while int(log10(a[1]) + 1) < 1000:
    a[0], a[1] = a[1], a[0] + a[1]
    i += 1

print(i)
print(time() - start)
