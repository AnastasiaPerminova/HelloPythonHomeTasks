# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
import random

list1 = [random.randint(-100, 100) for i in range(int(input('Введите количество элементов списка: ')))]
min = int(input('Введите минимум: '))
max = int(input('Введите максимум: '))
list2 = list()

print(list1)


for i in range(len(list1)):
    if min <= list1[i] <= max:
        list2.append(i)

print(list2)
