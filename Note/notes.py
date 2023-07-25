import datetime

date_now = datetime.datetime.now()

def read_file(filename):
    with open(filename, encoding='utf-8', errors='ignore') as file:
        data_array = []
        for line in file:
            data_array.append(line.replace('\n','').split(';'))
    return data_array 

def write_file(filename, data_array):
    with open(filename, 'w', encoding='utf-8', errors='ignore') as data:
        for i in data_array:
            write_element = '; '.join(i)
            data.write(f'{write_element}\n')

def menu():
   
    print('Добро пожаловать в ваши заметки!')
    print('1 - Показать все заметки')
    print('2 - Добавить заметку')
    print('3 - Найти заметку')
    print('4 - Изменить заметку')
    print('5 - Удалить заметку')
    user_operation = int(input())
            
    if user_operation == 1:
        show_all_notes(filename)
    elif user_operation == 2: 
        add_notes(filename)
    elif user_operation == 3: 
        find_notes(filename)
    elif user_operation == 4: 
        mod_notes(filename)
    elif user_operation == 5: 
        delete_notes(filename)

def show_all_notes(filename):
    data_array = read_file(filename)  
    for line in data_array:
        print("ID:", line[0], "\nТема:", line[1],"\nЗаметка:", line[2], "\nДата:", line[3]) 
        print('-----------------')  

def add_notes(filename):
    data_array = read_file(filename)
    max_id = 0
    for line in data_array:
        if int(line[0]) > max_id: 
            max_id = int(line[0])
    
    next_id = max_id + 1
    subject = input('Тема: ')
    note = input('Заметка: ')
    new_array = []
    new_array.append(str(next_id))
    new_array.append(subject)
    new_array.append(note)
    new_array.append(str(date_now))
   
    str(data_array.append(new_array))
    write_file(filename, data_array)           

def find_notes(filename):
    data_array = read_file(filename)
    print('По какой характеристике вы хотите осуществить поиск?')
    print('1 - ID')
    print('2 - Тема')
    print('3 - Дата')
   
    user_operation = int(input())
  
    if user_operation == 1:
        user_id = input("Введите ID записи: ")
        for line in data_array:
            if user_id in ''.join(line[0]): 
                print("ID:", line[0], "\nТема:", line[1],"\nЗаметка:", line[2], "\nДата:", line[3]) 
                print('-----------------')

    elif user_operation == 2: 
        user_subject = input("Введите Тему для поиска: ")
        for line in data_array:
            if user_subject in ''.join(line[1]):
                print("ID:", line[0], "\nТема:", line[1],"\nЗаметка:", line[2], "\nДата:", line[3]) 
                print('-----------------')       
    
    elif user_operation == 3: 
        user_date = input("Введите Дату(YYY-MM-DD HH:MM:SS) для поиска: ")
        for line in data_array:
            if user_date  in ''.join(line[2]): 
                print("ID:", line[0], "\nТема:", line[1],"\nЗаметка:", line[2], "\nДата:", line[3]) 
                print('-----------------')
                
    
    else:
        print("Вы ничего не ввели, или ввели непривильный номер")
        return find_notes(filename)

def mod_notes(filename):
    data_array = read_file(filename)
    user_subject = input("Введите Тему заметки, которую хотите изменить: ")
    
    for line in data_array:
        if user_subject in ''.join(line[1]):
            user_note = input('Введите новое содержимое заметки: ')
            line[2] = user_note
            line[3] = str(date_now)
            write_file(filename, data_array)
        
def delete_notes(filename):
    data_array = read_file(filename)  
    user_id = input('Введите ID записи, которую хотите удалить: ')   
    
    for line in data_array:
        if user_id in line[0]:
            data_array.remove(line)
            break
    
    write_file(filename, data_array) 

filename = 'NOTE.csv'
menu()