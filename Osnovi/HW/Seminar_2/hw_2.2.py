
frac2 = "17/15"
frac1 = "14/78"

import fractions
import math


chislitel_1 = int(frac1.partition('/')[0])
delitel_1 = int(frac1.partition('/')[2])

chislitel_2 = int(frac2.partition('/')[0])
delitel_2 = int(frac2.partition('/')[2])

summa_delitel = delitel_1 * delitel_2
summa_chislitel = ((summa_delitel // delitel_1) * chislitel_1) + ((summa_delitel // delitel_2) * chislitel_2)
common = math.gcd(summa_chislitel,summa_delitel)
while summa_chislitel % common == 0 and common != 1:
    summa_chislitel //= common

while summa_delitel % common == 0 and common != 1:
    summa_delitel //= common


proizvedenie_chislitel = chislitel_1 * chislitel_2
proizvedenie_delitel = delitel_1 * delitel_2
common = math.gcd(proizvedenie_chislitel,proizvedenie_delitel)
while proizvedenie_chislitel % common == 0 and common != 1:
    proizvedenie_chislitel //= common

while proizvedenie_delitel % common == 0 and common != 1:
    proizvedenie_delitel //= common

print(f'Сумма дробей: {summa_chislitel}/{summa_delitel}')
print(f'Произведение дробей: {proizvedenie_chislitel}/{proizvedenie_delitel}')

f1 = fractions.Fraction(chislitel_1,delitel_1)
f2 = fractions.Fraction(chislitel_2,delitel_2)

print(f'Сумма дробей: {f1 + f2}')
print(f'Произведение дробей: {f1 * f2}')