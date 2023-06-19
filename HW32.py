# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

a = int(input("Введите нижнюю границу списка: "))
b = int(input("Введите верхнюю границу списка: "))
n = int(input("Введите количество элементов списка: "))
min_array = int(input("Введите минимум: "))
max_array = int(input("Введите максимум: "))
array = [random.randint(a,b) for i in range(n)]
print(array)
print([i for i, num in enumerate(array) if min_array<num<max_array])