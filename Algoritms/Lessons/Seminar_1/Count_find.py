from random import randint
from time import time

UPPER = 1000

def  how_long(func_list, x):
    for func in func_list:
        start = time()
        func(x)
        print(f"Затраченное время {time() - start}")


def perebor(x):
    for i in range(1, UPPER + 1):
        if i == x:
            print(f"Число перебором за {i} шагов")
            break

def random_guess(x):
    k = 1
    guess = randint(1, UPPER)
    while guess != x:
        k += 1
        guess = randint(1, UPPER)
    print(f"случайно подобранное число за {k} шагов")

def smart_random(x):
    k = 1
    values = [i for i in range(1, UPPER + 1)]
    guess = randint(0, len(values) - 1 )
    while values.pop(guess) != x:
        k += 1
        guess = randint(0, len(values) - 1)
    print(f"Умное угадывание за {k} шагов")   

def binary_search(x): # это самый эффективный способ поиска чисел
    left = 1
    right = UPPER
    mid= (left + right) // 2
    k = 1
    while mid != x:
        if mid > x:
            right = mid - 1
        else:
            left = mid + 1
        k += 1
        mid= (left + right) // 2
    print(f"Бинарный поиск за {k} шагов")   

x = randint(1, UPPER)

func_list = []
# func_list.append(perebor)
# func_list.append(random_guess)
# func_list.append(smart_random)
func_list.append(binary_search)

how_long(func_list, x)