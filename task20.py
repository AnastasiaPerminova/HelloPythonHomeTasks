# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#  В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12

letters = {'A' : 1, 'a' : 1,
           'B' : 3, 'b' : 3, 
           'C' : 3, 'c' : 3,
           'D' : 2, 'd' : 2,
           'E' : 1, 'e' : 1,
           'F' : 4, 'f' : 4,
           'G' : 2, 'g' : 2,
           'H' : 4, 'h' : 4,
           'I' : 1, 'i' : 1, 
           'J' : 8, 'j' : 8,
           'K' : 5, 'k' : 5,
           'L' : 1, 'l' : 1,
           'M' : 3, 'm' : 3,
           'N' : 1, 'n' : 1,
           'O' : 1, 'o' : 1,
           'P' : 3, 'p' : 3,
           'Q' : 10, 'q' : 10,
           'R' : 1, 'r' : 1,
           'S' : 1, 's' : 1,
           'T' : 1, 't' : 1,
           'U' : 1, 'u' : 1, 
           'V' : 4, 'v' : 4,
           'W' : 4, 'w' : 4,
           'X' : 8, 'x' : 8,
           'Y' : 4, 'y' : 4,
           'Z' : 10,'z' : 10,
           'А' : 1, 'а' : 1,
           'Б' : 3, 'б' : 3,
           'В' : 1, 'в' : 1,
           'Г' : 3, 'г' : 3,
           'Д' : 2, 'д' : 2,
           'Е' : 1, 'е' : 1,
           'Ё' : 3, 'ё' : 3,
           'Ж' : 5, 'ж' : 5,
           'З' : 5, 'з' : 5,
           'И' : 1, 'и' : 1,
           'Й' : 4, 'й' : 4,
           'К' : 2, 'к' : 2,
           'Л' : 2, 'л' : 2,
           'М' : 2, 'м' : 2,
           'Н' : 1, 'н' : 1,
           'О' : 1, 'о' : 1,
           'П' : 2, 'п' : 2,
           'Р' : 1, 'р' : 1,
           'С' : 1, 'с' : 1,
           'Т' : 1, 'т' : 1,
           'У' : 2, 'у' : 2,
           'Ф' : 10, 'ф' : 10,
           'Х' : 5, 'х' : 5,
           'Ц' : 5, 'ц' : 5,
           'Ч' : 5, 'ч' : 5,
           'Ш' : 8, 'ш' : 8,
           'Щ' : 10, 'щ':  10,
           'Ь' : 3, 'ь' : 3,
           'Ы' : 4, 'ы' : 4,
           'Ъ' : 10, 'ъ' : 10,
           'Э' : 8, 'э' : 8,
           'Ю' : 8, 'ю' : 8,
           'Я' : 3, 'я' : 3}
           
word = input('Введите слово : ')
score = 0
for letter in word:
    for key in letters.keys():
        if letter == key:
            score += letters[key]

print(f'Стоимость введенного слова : {score}.')