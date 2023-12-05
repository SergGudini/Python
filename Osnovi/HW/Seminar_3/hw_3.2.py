# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд 
# (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов.

# import re
# from collections import Counter

# # Удаляем знаки препинания и приводим текст к нижнему регистру
# cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# # Разбиваем текст на слова и считаем их количество
# words = cleaned_text.split()
# word_counts = {}

# for word in words:
#     if word not in word_counts:
#         word_counts[word] = 1
#     else:
#         word_counts[word] += 1

# # Получаем 10 самых часто встречающихся слов
# top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# print(top_words)


text = "The quick brown 3.6 fox jumps over the lazy dog. Lazy dog, lazy fox!"

from collections import Counter
text = text.lower()

#text = text.replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '')
text = text.replace(str(range(0,9)), '')
text = text.replace("'", ' ')
text = text.replace(',', '')
text = text.replace('.', '')
text = text.replace('`', ' ')
text = text.replace('!', '')
text = text.replace('?', '')

words = text.split(' ')
for i in words:
    if i == '':
        words.remove('')     

words_count = Counter(words)
words_count = words_count.most_common(10)
print(words_count)
