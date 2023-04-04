def read_file(filename):
    lines = []
    with open(filename, encoding='utf-8', errors='ignore') as file:
        for line in file:
            lines.append(line.lower().strip())
    return lines 

def find_secret_array(lines):
    secret_array = []
    for line in lines:
        if 'subject: секретно,' in line:
            secret_array.append(line)
            if 'file: --"' in line: secret_array.remove(line)
        elif 'subject: секретно' in line:
            secret_array.append(line)
            if 'file: --"' in line: secret_array.remove(line)
        elif 'subject:секретно' in line:
            secret_array.append(line)
            if 'file: --"' in line: secret_array.remove(line)
  
    return secret_array # список состоит из только секретных сообщений и с вложенными файлами

def numbers_all(lines):
    secret_array = find_secret_array(lines)
    id_secret_array = []
    for line in secret_array:
        words = line.split()
        id_count = words[4]
        id_secret_array.append(id_count)
    
    id_secret_array = list(set(id_secret_array))
   
    return id_secret_array # список из индивидуальних id сообщений

def numbers_sources_adress(lines, domain = ''):
    secret_array = find_secret_array(lines)
    start_word = 'from:'
    stop_word = 'subject:'
    sources_list = []
    
    for line in secret_array:
        words = line.split()
        id_count = words[4]
        start_index = line.index(start_word)
        stop_index = line.index(stop_word)
        if start_index <= stop_index:
            sources_list.append(id_count + ' ' + line[start_index + 6:stop_index])
        else:
            sources_list.append(id_count + ' ' + line[stop_index + 6:start_index][::-1])
    
    sources_list = list(set(sources_list))
    count = 0
    
    for line in sources_list:
        if domain in line: count += 1
     
    #print('\n'.join(sources_list)) 
                   
    return count # число отправленных сообщений в зависимости от введенного домена

def numbers_destination_adress(lines, domain = ''):
    secret_array = find_secret_array(lines)
    start_word = 'to:'
    stop_word = 'from:'
    destination_list = []
    
    for line in secret_array:
        words = line.split()
        id_count = words[4]
        start_index = line.index(start_word)
        stop_index = line.index(stop_word)
        if start_index <= stop_index:
            destination_list.append(id_count + ' ' + line[start_index + 6:stop_index])
        else:
            destination_list.append(id_count + ' ' + line[stop_index + 6:start_index][::-1])
    
    destination_list = list(set(destination_list))
    count = 0
    
    for line in destination_list:
        if domain in line: count += 1
     
    #print('\n'.join(sources_list)) 
                   
    return count # число полученных сообщений в зависимости от введенного домена


   
file = input('Введите имя файла: ')
domain = input('Введите свой домен: ')
lines = read_file(file)
print('\n'.join(find_secret_array(lines)))
print(f'Всего секретных сообщений: {len(numbers_all(lines))}')
print(f"Всего отправленных сообщений от {domain}: {numbers_sources_adress(lines,domain)}")
print(f"Всего полученных сообщений от {domain}: {numbers_destination_adress(lines,domain)}")