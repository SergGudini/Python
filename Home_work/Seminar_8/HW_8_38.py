def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            data_array.append(line.replace('\n','').split(','))
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ', '.join(i)
            data.write(f'{write_element}\n')

def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Найти запись')
    print('4 - Изменить запись')
    print('5 - Удалить запись')
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2: 
        add_item(filename)
    elif user_operation == 3: 
        find_item(filename)
    elif user_operation == 4: 
        mod_item(filename)
    elif user_operation == 5: 
        delete_item(filename)

def show_all_items(filename):
    data_array = read_file(filename)  
    for i in range(1,len(data_array)):
        print("ID:", data_array[i][0], "   Фамилия:", data_array[i][1],"   Имя:", data_array[i][2], "   Отчество:", data_array[i][3], "   Телефон:", data_array[i][4])

def add_item(filename):
    data_array = read_file(filename)
    max_id = 0
    for i in range(1,len(data_array)):
        if int(data_array[i][0]) > max_id: max_id = int(data_array[i][0])
    
    next_id = max_id + 1
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ') 
    new_array = []
    new_array.append(str(next_id))
    new_array.append(lastname)
    new_array.append(firstname)
    new_array.append(secondname)
    new_array.append(phone)

    data_array.append(new_array)
    write_file(filename, data_array)   

def find_item(filename):
    data_array = read_file(filename)
    print('По какой характеристике вы хотите осуществить поиск?')
    print('1 - ID')
    print('2 - Фамилия')
    print('3 - Имя')
    print('4 - Отчество')
    print('5 - Телефон')
   
    user_operation = int(input())
  
    if user_operation == 1:
        user_id = input("Введите ID записи: ")
        for line in data_array:
            if user_id in ''.join(line): 
                print('ID   lastname   firstname   secondname   phone')
                print(', '.join(line))

   
    elif user_operation == 2: 
        user_lastname = input("Введите Фамилию для поиска: ")
        for line in data_array:
            if user_lastname in ''.join(line):
                print('ID   lastname   firstname   secondname   phone')
                print(', '.join(line))       
    
    elif user_operation == 3: 
        user_firstname = input("Введите Имя для поиска: ")
        for line in data_array:
            if user_firstname in ''.join(line): 
                print('ID   lastname   firstname   secondname   phone')
                print(', '.join(line))
    
    elif user_operation == 4: 
        user_secondname = input("Введите Отчество для поиска: ")
        for line in data_array:
            if user_secondname in ''.join(line): 
                print('ID   lastname   firstname   secondname   phone')
                print(', '.join(line))
    
    elif user_operation == 5: 
        user_phone = input("Введите Телефон для поиска: ")
        for line in data_array:
            if user_phone in ''.join(line): 
                print('ID   lastname   firstname   secondname   phone')
                print(', '.join(line))
    
    else:
        print("Вы ничего не ввели, или ввели непривильный номер")
        return find_item(filename)

def mod_item(filename):
    data_array = read_file(filename)  
    user_id = input('Введите ID записи, которую хотите изменить: ')
 
    print('По какой характеристике вы хотите осуществить изменение?')
    print('1 - Фамилия')
    print('2 - Имя')
    print('3 - Отчество')
    print('4 - Телефон')
    user_operation = int(input())
    
    for i in range(len(data_array)):
        if user_id in data_array[i][0]:
            user_id_index = i
            break
        
    if user_operation == 1: 
        user_lastname = input("Введите Фамилию: ")
        data_array[user_id_index][1] = user_lastname
        write_file(filename, data_array)      
            
    elif user_operation == 2: 
        user_firstname = input("Введите Имя: ")
        data_array[user_id_index][2] = user_firstname
        write_file(filename, data_array)  
            
    elif user_operation == 3: 
        user_secondname = input("Введите Отчество: ")
        data_array[user_id_index][3] = user_secondname
        write_file(filename, data_array) 
            
    elif user_operation == 4: 
        user_phone = input("Введите Телефон: ")
        data_array[user_id_index][4] = user_phone
        write_file(filename, data_array) 
            
    else:
        print("Вы ничего не ввели, или ввели непривильный номер")
        return find_item(filename)

def delete_item(filename):
    data_array = read_file(filename)  
    user_id = input('Введите ID записи, которую хотите удалить: ')   
    
    for i in range(len(data_array)):
        if user_id in data_array[i][0]:
            user_id_index = i
            break
    
    data_array.remove(data_array[user_id_index])
    
    write_file(filename, data_array) 

filename = 'file.txt'
menu()