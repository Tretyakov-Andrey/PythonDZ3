# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]



def fib(n):
    a, b = 0, 1
    for i in range(n+1):
        yield a
        a, b = b, a + b

dataone = list(fib(8))

def fibdif(n):
    a, b = 1, -1
    for i in range(n):
        yield a
        a, b = b, a - b

datatwo = list(fibdif(8))
datatwo.reverse()

data = datatwo + dataone
print(data)

