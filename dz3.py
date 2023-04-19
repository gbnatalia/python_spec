'''
Создайте функцию генератор чисел Фибоначчи
'''

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    f = fibonacci()
    for i in range(10):
        print(next(f))