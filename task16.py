# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3

# -> 1
import random

n = int(input('Введите число N - количество элементов в массиве: '))
list_1 = list()

for i in range(n):
    number = random.randint(0, 10)
    list_1.append(number)

print(list_1)

x = int(input('Введите число X : '))
count = 0

for number in list_1:
    if number == x:
        count += 1

print(f'Число {x} встречается в списке {count} раз.')
