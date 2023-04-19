'''
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
'''
import os

def parse_path(path):
    file_path, file_name = os.path.split(path)
    file_name, file_ext = os.path.splitext(file_name)
    return file_path, file_name, file_ext

if __name__=="__main__":
    path = '/home/user/documents/file.txt'
    print(parse_path(path))

    path = 'C:/Users/user/Pictures/flower.jpg'
    print(parse_path(path))
