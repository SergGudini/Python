"""Задача №25. Решение в группах Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n.
Для решения данной задачи используйте функцию .split()

letters = "a a a b c a a d c d d"
dict_letters = {}
result_string = ""

letters = letters.split(" ")

for i in range(len(letters)):
    if dict_letters.get(letters[i]) == None:
        dict_letters[letters[i]] = 0
        result_string += f"{letters[i]}"
    else:
        dict_letters[letters[i]] += 1
        result_string += f"{letters[i]}_{dict_letters[letters[i]]}"
print(result_string)
"""
"""Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.

text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

dict_text = {}
result = 0

splited_text = text.lower().split(" ")

for i in range(len(splited_text)):
    if dict_text.get(splited_text[i]) == None:
        dict_text[splited_text[i]] = 1
        result += 1
print(result)
"""

"""Война и мир количество слов"""
import fileinput

count = 0
date = {}
source = {}
file = {}
temp_strip = []


with open('maillog_1.txt', encoding='utf-8', errors='ignore') as f:
    
    # text хранит строки без пробелов и символов
    #text = f.read().lower().strip().replace('.','').replace(',', '').replace(':', '').replace('!', '').replace('?', '')
    text = f.read().lower()
    
    #print(len(text.split()))
    #print(len(text.strip()))
    
    text_split = text.split() # слова
    text_strip = text.strip() # строки
    
    for i in range(len(text.strip())):
        print(len(text.strip().split()))
    
    #print(text_split[0:len(text.split())])
    #print(text.rstrip("\n").split(" "))
    #text_split = text.split()
    #print(len(text))
        
    #for i in range(len(text_split)):
        #if text_split[i] == 'jan':
        #    date = text_split[i] + text_split[i+1] + text_split[i+2]
        #if text_split[i] == 'from':
        #    source = text_split
            
       # if text_split[i] == 'секретно':
        #    print(date, ' ', text_split)
        #    count += 1
        #if text.rstrip("\n").split("dragun@gomu.gs.vs.mil.by"):
        
print(count)    
        
    #print(len(text.strip()))
    #for i in range(len(text.strip())):
        #for j in range(len(text.split())):
           # if (text.split[j] == word):
               # print(text.strip[i])
        
    
    