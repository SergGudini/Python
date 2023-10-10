def enter_float():
    value = 0.0
    while True:
        try:          
            value = input('Введите дробное число: ')
            float(value) == value
            break
        except ValueError:
            print ('Это не дробное число. Введите заново.')
            continue
    return value
     
enter_float()