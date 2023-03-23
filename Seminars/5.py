# Фибоначи
"""def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)  # [1, 1, 2, 3, 5, 8, 13, 21, 34]"""

# Задача №33. Хакер Василий получил доступ к классному журналу и 
# хочет заменить все свои минимальные оценки на 
# максимальные. Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.

"""import random

def zhurnal(n):
    temp = ()
    for i in range(n):
        temp = random.randint(1,5)
    return temp"""

# Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
"""import math
def easy_number(number):
    i = 2
    flag = 1
    #while i < number:
        #if number % i == 0:
            #flag = 0
            #break
    while i < math.sqrt(number):
        if number % i == 0:
            flag = 0
            break
        i += 1
    if flag == 0: print("Не простое", number)
    else: print("Простое", number)

print(easy_number(103))"""

# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке. 
# Примечание. В программе запрещается объявлять массивы и использовать 
# циклы (даже для ввода и вывода).

num = [3,4,5]
# print(sorted(num, reverse=True))

# print(num[::-1])

def super_recurse():    
    number = input()
    if number != '':
        super_recurse()
    print(number)

super_recurse()