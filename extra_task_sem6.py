# Даны числа a и b.Выяснить, какое из них больше,
#  не применяя никаких операторов сравнения. if == <> =!

a = int(input('a = '))
b = int(input('b = '))
max = (a + b + abs(a - b))//2
min = (a + b - abs(a - b ))//2
print('max = ', max, 'min = ', min)
