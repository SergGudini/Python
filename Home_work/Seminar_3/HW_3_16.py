# Задача 16. Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое 
# необходимо проверить - X. Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

import random

n = int(input('Введите размер массива: '))

array = [random.randint(1,(n//2)) for i in range(n)]
print('Ваш массив', array)

x = int(input('Введите число, которое необходимо проверить: '))
count = 0

for i in range(n):
    if array[i] == x:
        count += 1
print(f'{x} встречается {count} раз(а)')