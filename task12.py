# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

sum = int(input('Введите сумму двух натуральных чисел X и Y  (X,Y≤1000): '))
product = int(input('Введите произведение двух натуральных чисел X и Y  (X,Y≤1000): '))

if sum > 2000 or product > 1000000:
    print ('Введенные значения не соответствуют условию.')
else:
    find = False
    for x in range(1, sum-1):
        y = sum - x
        if product == y * x:    
            find = True
            print(f'Задуманные Петей числа это {x} и {y}.')
            break
    if find == False:
        print('Решение невозможно.')

