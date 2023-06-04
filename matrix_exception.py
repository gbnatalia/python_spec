'''
Для класса Матрица с методами для вывода на печать, сравнения,
сложения, транспонирования, умножения матриц
Написать классы исключения с выводом подробной информации.
Поднимать исключения внутри основного кода
'''

class MatrixException(Exception):
    pass


class MatrixClassError(MatrixException):

    def __init__(self, matrix, func_name):
        self.matrix = matrix
        self.prefix = f"Ошибка в функции {func_name}. "

    def __str__(self):
        return f"{self.prefix}Переданный объект не является объектом класса Matrix"


class MatrixTypeDataError(MatrixException):
    def __init__(self, func_name, m):
        self.m = m
        self.prefix = f"Ошибка в функции {func_name}. "

    def __str__(self):
        if self.m == None:
            return f"{self.prefix}Значение матрицы не должно быть нулевым!"
        elif not isinstance(self.m, list):
            return f"{self.prefix}Матрица должна определяться как список списков!"
        elif not len(self.m):
            return f"{self.prefix}Матрица не может иметь 0 строк!"
        elif not isinstance(self.m[0], list):
            return f"{self.prefix}Матрица должна определяться как список списков!"
        elif not len(self.m[0]):
            return f"{self.prefix}Матрица не может иметь 0 колонок!"
        else:
            for row in self.m:
                for el in row:
                    if not isinstance(el, int):
                        return f"{self.prefix}Все элементы матрицы должны быть целыми числами!"


class MatrixSizeError(MatrixException):

    def __init__(self, m1, m2, func_name):
        self.prefix = f"Ошибка в {func_name}. "
        self.m1 = m1
        self.m2 = m2

    def __str__(self):
        if len(self.m1) != len(self.m2):
            return f"{self.prefix}.Число строк для каждой матрицы должно совпадать!"
        elif len(self.m1[0]) != len(self.m2[0]):
            return f"{self.prefix}Число столбцов для каждой матрицы должно совпадать!"

