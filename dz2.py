'''
Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.
'''

def my_func(**kwargs):
    my_dict = {}
    for k, v in kwargs.items():
        if isinstance(k, (str, int, float, bool)):
            my_dict[k] = v
        else:
            my_dict[str(k)] = v
    return {v: k for k, v in my_dict.items()}

if __name__=="__main__":
    result = my_func(name='John', age=25, married=True)
    print(result)
