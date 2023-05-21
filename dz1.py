'''
Напишите следующие функции:
- Нахождение корней квадратного уравнения
- Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
- Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
- Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл.
'''
from typing import Callable
from pathlib import Path
import csv
import random
import json

def generate_csv_file(filename):
    '''
    Генерация csv файла с тремя случайными числами в каждой строке.
    100-1000 строк.
    '''
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        cnt_string = random.randint(100, 1001)
        for i in range(cnt_string):
            row = [random.randint(1, 100) for _ in range(3)]
            writer.writerow(row)


def save_decoration(func: Callable):
    '''
    Декоратор, сохраняющий переданные параметры и результаты работы
    функции в json файл.
    '''
    filename = Path(f"{func.__name__}.json")
    if filename.exists():
        with open(filename, 'r', encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    def wrapper(*args):
        result = func(*args)
        with open(filename, 'w', encoding="utf-8") as file:
            data.append({'args': args, 'solution': str(result) if result != None else "None"})
            json.dump(data, file, indent=4)
    return wrapper


def solution_decoration(func: Callable): 
    '''
    Декоратор, запускающий функцию нахождения корней квадратного
    уравнения с каждой тройкой чисел из csv файла.
    '''
    filename = 'random_numbers.csv'
    generate_csv_file(filename)   
    def wrapper():  
        nonlocal filename  
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                a, b, c = row                    
                roots = func(a, b, c)
        print("операция выполнена!")
        return roots
    return wrapper            


@solution_decoration
@save_decoration
def find_solution(*args):
    '''
    Нахождение корней квадратного уравнения
    ax^2 + bx + c = 0
    '''  
    if len(args) < 3:
        return None
    
    a, b, c = args
    a = int(a)
    b = int(b)
    c = int(c)

    if a == 0 and b == 0 and c == 0:
        return '00'
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return (-b / (2*a),)
    else:
        return ((-b + discriminant**0.5) / (2*a), (-b - discriminant**0.5) / (2*a))

		
if __name__ == "__main__":
    find_solution()

       

