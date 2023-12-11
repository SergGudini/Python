# Напишите функцию key_params, принимающую на вход только ключевые параметры и 
# возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def key_params(**arg):
    new_params = {}
    for key, value in arg.items():
        if value == None:
            new_params[str(value)] = key
        if hashable(value) and value != None:
            new_params[value] = key
        else:
            new_params[str(value)] = key
        
    return new_params

def hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

#params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
params = key_params(a = None, b = '', c = [], d = {})
print(params)