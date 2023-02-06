# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

import random

n = int(input('Введите число N - количество элементов в массиве: '))
list_1 = list()

for i in range(n):
    number = random.randint(0, 100)
    list_1.append(number)

print(list_1)

x = int(input('Введите число X : '))
delta_min = 100
nearest_number = None
nearest_number_2 = None

for number in list_1:
    if abs(number - x) < delta_min:
        delta_min = abs(number - x)
        nearest_number = number

for number in list_1:
    if abs(number - x) == delta_min and number != nearest_number:
        nearest_number_2 = number

if nearest_number_2 == None:
    print(f'В списке самый близкий по величине элемент к заданному числу {x} - число {nearest_number}.')
else:
    print(f'В списке самые близкие по величине элементы к заданному числу {x} - числа {nearest_number} и {nearest_number_2}.')
    