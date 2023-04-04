"""import threading
 
def proc(n):
   print ("Процесс",n)
 
p1 = threading.Thread(target=proc(1))#, name="t1", args=["3"])
p2 = threading.Thread(target=proc(2))#, name="t2", args=["2"])
p1.start()
p2.start()"""

import threading
import requests
import time

def connect(url):
    res = requests.get(url)
    connection_status = res.status_code
    #if 100 <= connection_status <= 199: return (f'{url} Код ответа "Информационный" - {connection_status}')
    #if 200 <= connection_status <= 299: return (f'{url} Код ответа "Успех" - {connection_status}')
    #if 300 <= connection_status <= 399: return (f'{url} Код ответа "Перенаправление" - {connection_status}')
    #if 400 <= connection_status <= 499: return (f'{url} Код ответа "Ошибка клиента" - {connection_status}')
    #if 500 <= connection_status <= 599: return (f'{url} Код ответа "Ошибка сервера" - {connection_status}')
    return connection_status

numbers_requests = int(input('Введите количество URL запросов: '))
numbers_connections = int(input('Введите количество одновременных запросов: '))
input_url = input('Введите URL запрос: ')
url = []

for i in range(numbers_requests):
   url.append(input_url)
   
#print('Ваши адреса', url)

start = time.time()
for i in url:
   connect(i)
print(f'Последовательное выполнение запросов: {time.time() - start : .2f} seconds')

start = time.time() # Начало для одновременного выполнения всех URL запросов

all_threads = []
for k in range(numbers_connections):
   for i in url:
      count_thread = threading.Thread(target=connect, args=(i,))
      count_thread.start()
      all_threads.append(count_thread)

   for count_thread in all_threads:
      count_thread.join()
         
# start = time.time() # Начало для одновременного выполнения всех URL запросов

# all_threads = []

# for i in url: # одновременный запрос всех url от одного пользователя
#    count_thread = threading.Thread(target=connect, args=(i,))
#    all_threads.append(count_thread)
#    count_thread.start()
# for count_thread in all_threads:
#    count_thread.join()

print(f'Одновременное выполнение запросов: {time.time() - start : .2f} seconds')


#print(res.status_code)
#print(res.headers)
#print(res.text)
