def null_value():
    value = None
    while True:
        try:          
            value = input('Введите что-нибудь: ') # raw_input in Python 2.x
            if not value:
                raise ValueError('Пустая строка.')
        except ValueError as e:
            print(e)
            continue
    

null_value()