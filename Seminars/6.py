# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом 
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, 
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы 
# второго массива
"""
n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))

array_1 = set({input() for i in range(n)})
array_2 = set({input() for i in range(m)})

difference_array = array_1.difference(array_2)

print(difference_array)
"""

# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество 
# элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
"""
import random

size = int(input("Введите размер массива: "))

list_1 = list()
count = int(0)
for x in range(size):
    r = random.randint(1, size / 2)
    list_1.append(r)
print(list_1)
x = 1
for x in range(size-1):
    if list_1[x] > list_1[x-1] and list_1[x] > list_1[x+1]:
        count +=1

print(count)
"""

# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два 
# элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. 
# Все числа списка находятся на разных строках.

numbers = [2,5,4,6,7,8,5,7,2,4]
size = int(len(numbers))
j = 1
for i in range(size - 1):
    count_number = numbers[i]
    print(numbers)
    
    for j in range(size):
        if numbers[j] == count_number:
            numbers.pop(j)
            numbers.pop(i)
            size -= 2
            break
            
    