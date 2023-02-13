# Задача 28: Напишите рекурсивную функцию sum(a, b),
#  возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# 2 2
# 4

def sum(a,b):
    if b == 0:
        return a
    b = b - 1
    a = a + 1
    return sum (a,b)

a = int(input('Введите неотрицательное число a: '))
b = int(input('Введите неотрицательное число b: '))

if a < 0 or b < 0:
    print ('Ошибка ввода')
else:
    print(f'Сумма чисел : {sum(a, b)}')
    