"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y
(X,Y?1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате
отгадать задуманные Петей числа."""

import random

numberPetr1 = random.randint(1,1000)
numberPetr2 = random.randint(1,1000)
numberKate1 = 0
numberKate2 = 0

summa = numberPetr1 + numberPetr2
proizvedenie = numberPetr1 * numberPetr2

for i in range(1000):
    for j in range(1000):
        if summa == i + j and proizvedenie == i * j:
            numberKate1 = i
            numberKate2 = j

print('Катя, Петя загадал числа (',numberKate2,',',numberKate1,')')
print('Петины числа (',numberPetr1,',',numberPetr2,')')
