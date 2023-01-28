# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите трехзначное число: '))

if number < 99 or number > 999:
    print('Необходимо было ввести трехзначное число.')
else:
    sum = 0
    number_modified = number
    while number_modified > 0:
        digit = number_modified % 10
        number_modified = number_modified // 10
        sum = sum + digit
  

print(f'Сумма цифр числа {number} равна {sum}.')
