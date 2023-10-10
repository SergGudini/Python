import datetime
class Error:
    strError = 'StrError: Получены некорректные данные, ФИО должны иметь строковый тип!'
    indexError = 'IndexError: Получено некорректное кол-во данных!'
    dateError = 'DateError: Получен некорректный формат даты. Формат даты: dd.mm.YYYY, н-р: 01.01.2000!'
    numberError = 'NumError: Введен некорректный номер телефона. Формат номера: 89--------- и длина 11 символов!'
    genderError = 'GenError: Данные полученные о поле, некорректны, необходимо указать либо: m - мужчина, либо f - женщина!'
    writeReadError = 'FileError: Непредвиденные проблемы с чтением-записью в файл. Обратитесь в тех. поддержку, по номеру: ' \
                     '88005553535, ведь лучше позвонить, чем у кого-то занимать!'
def check_user_name(val):
    try:
        str(val)
        try:
            int(val)
            return False
        except:
            try:
                float(val)
                return False
            except:
                return True
    except:
        return False
def check_birthdate(date):
    try:
        datetime.datetime.strptime(date, '%d.%m.%Y')
        return True
    except:
        return False
def check_phone_num(num):
    if len(str(num)) == 11:
        if list(str(num))[0] == '8' and list(str(num))[1] == '9':
            return True
        else:
            return False
    else:
        return False

def check_gender(val):
    if val == 'm' or val == 'f':
        return True
    else:
        return False
print('Приступим к регистрации, пожалуйста укажите ваши: Фамилия, Имя, Отчество, дата рождения, номер телефона, пол\n'
      '• Инструкция по заполнению:\n'
      '• Форматы данных:\n'
      '» фамилия, имя, отчество - строки\n'
      '» датарождения - строка формата dd.mm.yyyy\n'
      '» номертелефона - целое беззнаковое число без форматирования\n'
      '» пол - символ латиницей f или m.\n')
user_data = input('Пожалуйста введите ваши данные (через пробел): ')
dict_data = user_data.split(' ')
while len(dict_data) != 6:
    print(f'{Error.indexError} Кол-во указанных Вами данных: {len(dict_data)}, а нам нужно 6, попробуйте снова.')
    user_data = input('Пожалуйста введите ваши данные: Фамилия, Имя, Отчество, дата рождения, номер телефона, пол - через пробел!: ')
    dict_data = user_data.split(' ')
while check_user_name(dict_data[0]) != True:
    print(Error.strError)
    user_data = input('Пожалуйста введите ваши данные: Фамилия, Имя, Отчество, дата рождения, номер телефона, пол - через пробел!: ')
    dict_data = user_data.split(' ')
while check_user_name(dict_data[1]) != True:
    print(Error.strError)
    user_data = input('Пожалуйста введите ваши данные: Фамилия, Имя, Отчество, дата рождения, номер телефона, пол - через пробел!: ')
    dict_data = user_data.split(' ')
while check_user_name(dict_data[2]) != True:
    print(Error.strError)
    user_data = input('Пожалуйста введите ваши данные: Фамилия, Имя, Отчество, дата рождения, номер телефона, пол - через пробел!: ')
    dict_data = user_data.split(' ')
while check_birthdate(dict_data[3]) != True:
    print(Error.dateError)
    user_data = input('Пожалуйста введите ваши данные: Фамилия, Имя, Отчество, дата рождения, номер телефона, пол - через пробел!: ')
    dict_data = user_data.split(' ')
while check_phone_num(dict_data[4]) != True:
    print(Error.numberError)
    user_data = input('Пожалуйста введите ваши данные: Фамилия, Имя, Отчество, дата рождения, номер телефона, пол - через пробел!: ')
    dict_data = user_data.split(' ')
while check_gender(dict_data[5]) != True:
    print(Error.genderError)
    user_data = input('Пожалуйста введите ваши данные: Фамилия, Имя, Отчество, дата рождения, номер телефона, пол - через пробел!: ')
    dict_data = user_data.split(' ')
try:
    with open(f'{dict_data[0]}.txt', 'a') as info:
        info.writelines(user_data+'\n')
        print('Данные о пользователе сохранены!')
except:
    print(Error.writeReadError)