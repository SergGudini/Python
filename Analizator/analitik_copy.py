import os,re,sys

count = 0
file_out = 0
source_index = 0
destination_index = 0
file_index = 0
subject_index = 0
id_message_index = 0

with open('maillog2.txt', encoding='utf-8', errors='ignore') as file:
    result_file = open('result.txt','w')
    line = file.readlines() # создание списка из строк исходного файла
    size = len(line)
    
    for i in range(len(line)):
        word = line[i].lower().split() # каждая строка разбивается на слова без пробела и преобразуется в нижний регистр
        for_id = line[i+1].lower().split()

        if word[4] != for_id[4]: count += 1

        for j in range(len(word)): # поиск секретных сообщений в строке
             
            if (word[j] == 'секретно' and word[j-1] != 'не') or (word[j] == 'секретно' and word[j-1] != 'не') or (word[j] == 'секретно,' and word[j-1] != 'не') or (word[j] == 'секретно.' and word[j-1] != 'не') or (word[j] == 'секретно!' and word[j-1] != 'не'):
                #count += 1
                
                for k in range(len(word)): # в случае нахождения слова cекретно, проходим еще раз и достаем необходимые параметры сообщения
                    
                    if word[k] == 'from:': source_index = k         # индекс адреса отправителя
                    if word[k] == 'to:': destination_index = k      # индекс адреса получателя
                    if word[k] == 'file:': file_index = k           # индекс файла отправителя
                    if word[k] == 'subject:': subject_index = k     # индекс темы отправителя
                    if 'exim[' in word[k]: id_message_index = k     # индекс id сообщения отправителя

                    id_message = word[id_message_index]                             # id сообщения отправителя
                    destination_address = word[destination_index+1:source_index]    # адреса получателя (слова от индекса получателя до индекса отправителя)
                    source_adress = word[source_index+1:subject_index]              # адреса отправителя (слова от индекса отправителя до индекса темы)
                    subject = word[subject_index+1:file_index]                      # тема сообщения (от индекса сообщения до индекса файла)
                    file_mail = word[file_index+1:len(word)]                        # файл сообщения (от индекса файла сообщения до конца строка)
                    date = word[0:3]                                                # дата сообщения (позиции неизменны)

                # вывод параметров секретного сообщения с пребразованием из обратно в строку
                print(' '.join(date), ''.join(id_message))
                print('ОТПРАВИТЕЛЬ:', ' '.join(destination_address),'ПОЛУЧАТЕЛЬ:', ' '.join(source_adress),'ТЕМА:',' '.join(subject), 'ФАЙЛ:',' '.join(file_mail))      
    
    

print('\nВсего секретных сообщений за сегмент: ', (count - file_out))
file.close()

