# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться 
# в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух 
# вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке

#stih = 'пара-ро-рам рам-пам-пупам па-ра-па-дам'
stih = input('Винн-Пух говорит: ')
glasnie = ['у','е','ы','а','о','э','я','и','ю']

#count = stih_split[0].count(glasnie.strip(glasnie[0]))
stih_split = stih.split()
count = []
count_word = []
#print(stih_split[0].count('уеыаоэяию'))
for i in stih_split:
    count_word = [0]
    for j in glasnie:
        if i.count(j) != 0:
            count_word.append(i.count(j))
    count.append(sum(count_word))          
print(count)
if len(set(count)) == 1: print('Парам пам-пам')
else: print('Пам парам')


"""string = 'пара-ра-рам ром-пюм-папам па-ра-па-дам'
letter = 'аеёиоуэюя'
arr = string.split(' ')

list1 = []
for i in arr:
    count = 0
    for j in range(1, len(i)):
        if i[j] in letter:
            count+=1
    list1.append(count)

if len(set(list1))==1:
    print('Парам пам-пам')
else:
    print('Пам парам')
    
string = 'пара-пара-рам прамар-рамар-пар па-па-рама-ра'
array = string.split()
count = array[0].count('а')
for i in range(len(array)):
     if array[i].count('а') == count:
         continue
     else:
         break
         print("парам-пам")
else:
    print("парм-пам-пам")"""
