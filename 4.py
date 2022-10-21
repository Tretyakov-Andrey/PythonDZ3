# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10 

from math import floor

x = 100

res = []

while x != 0:
    if x%2 == 0:
        res.append(0)
    else: res.append(1)
    x = floor(x/2)
res.reverse()

print(res)

