num = 123456
number = num
predstavlenie = list('0123456789ABCDEF')
result = list()

while num > 0:
    result.append(predstavlenie[num % 16])
    num //= 16

print('Шестнадцатеричное представление числа: ' + ''.join(result[::-1]))
print(f'Проверка результата: {hex(number)}')

