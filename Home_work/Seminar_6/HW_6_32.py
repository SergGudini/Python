# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

size = int(input('Введите размер массива: '))
array = [random.randint(-100,100) for i in range(size)]
min = random.randint(-100,100)
max = random.randint((min + 1),100)

print('Ваш массив: ', array)
print(f'[{min},{max}]')

for i in range(len(array)):
    if min <= array[i] <= max:
        print(i)
        
