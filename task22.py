# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите n - количество элементов первого множества: '))
m = int(input('Введите m - количество элементов второго множества: '))
set_1 = set()
set_2 = set()

for i in range(n):
    number = float(input(f'Введите {i + 1}е число первого множества '))
    set_1.add(number)

print()

for i in range(m):
    number = float(input(f'Введите {i + 1}е число второго множества '))
    set_2.add(number)

print(set_1)
print(set_2)

set_result = set_1.intersection(set_2)
list_result = list(set_result)
list_result.sort()

print(list_result)
