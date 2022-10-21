# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

_list = [1.1, 1.2, 3.1, 5, 10.01]
_iwantnewspisok = []

for i in range(len(_list)):
    _iwantnewspisok.append(_list[i] - round(_list[i]))

_min = min(_iwantnewspisok)
_max = max(_iwantnewspisok)

res = _max - _min

print(f'{res}')
