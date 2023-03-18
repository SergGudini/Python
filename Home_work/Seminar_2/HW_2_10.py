"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть"""

import random

n = int(input('Введите количество монеток n: '))

"""Изначально все монеты лежат Гербом вверх"""
moneta = ['(Г)' for i in range(n)]

count_reshka = 0

"""А здесь пришел младший брат и перевернул несколько монет Решкой вверх"""

for i in range(n):
    
    temp = random.randint(0,1)
    if temp == 0:
        moneta[i] = '(Р)'
        count_reshka = count_reshka + 1

count_gerb = n - count_reshka

print('Наши монеты на столе')
print(moneta)
print('Количество монет Гербом вверх: ', count_gerb)
print('Количество монет Решкой вверх: ', count_reshka)

"""Проверка сколько монет надо перевернуть. Если Решко меньше, переворачиваем их,
в противном случае, переворачиваем Гербы"""

if count_reshka < count_gerb and count_gerb != n and count_reshka != n:
    print('Надо перевернуть Решко в количестве: ', count_reshka)
elif count_reshka > count_gerb and count_gerb != n and count_reshka != n:
    print('Надо перевернуть Герб в количестве: ', count_gerb)
elif count_reshka == count_gerb:
    print('Можно перевернуть все, что угодно')
elif n == 0: print('Вы ввели неправильное значение монет')
else: print('Ничего переворачивать не надо')
