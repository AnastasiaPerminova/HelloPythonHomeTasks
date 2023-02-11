#В одной компьютерной игре игрок выставляет в линию шарики разных цветов. 
#Когда образуется непрерывная цепочка из трех и более шариков одного цвета, она удаляется из линии. 
# Все шарики при этом сдвигаются друг к другу, и ситуация может повториться.
#Напишите программу, которая по данной ситуации определяет, сколько шариков будет "уничтожено".
# Естественно, непрерывных цепочек из трех и более шаров в начальный момент может быть не более одной.
#Входные данные:
#Сначала вводится количество шариков в цепочке(не более 1000) и цвета шариков(от 0 до 9, каждому цвету соответствует свое целое число).
# Выходные данные:
# Требуется вывести количество шариков, которое будет "уничтожено".

def delete_balls(list):
    cont = None
    for i in range(len(list) - 2):
        if list[i] == list[i + 1] == list[i + 2]:
            cont = True
    count = 0
    sum = 0
    indexes = []
    if cont == True:
        for i in range(len(list) - 1):
            if list[i] == list[i + 1]:
                count += 1               
            else:
                if count >= 2:
                    sum += count + 1
                    for j in range (i - count, i+1):
                        indexes.append(j)
                count = 0
        k = 0           
        for element in indexes:
            list.pop(element - k)
            k += 1
        print(f'После удаления шаров одного цвета: {list}')
        print(f'Удалено {sum}')
        return delete_balls(list) + sum
    return 0
    
list_1 = [1, 1, 2, 7, 5, 6, 3, 3, 3, 3, 3, 6, 6, 5, 7, 7, 1, 2, 6]
print(list_1)
print(f'Всего удалено {delete_balls(list_1)}')
    
    


