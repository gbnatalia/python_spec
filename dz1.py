'''
Создайте класс Матрица. Добавьте методы для:
- вывода на печать,
- сравнения,
- сложения,
- транспонирования,
- умножения матриц
'''

import numpy as np
import inspect


class Matrix:

    def __init__(self, m):
        self.m = m
        self.rows = len(m)
        self.cols = len(m[0])


    def __str__(self) -> str:
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.m])


    def __repr__(self) -> str:
        return f'"Matrix({self.m})"'


    def _matrix_validate(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'Параметр функции {inspect.stack()[1][3]} должен быть типа Matrix')


    def _size_validate(self, other):
        if not self.cols or not self.rows:
            raise ValueError(f'Некорректные размеры матриц в операции {inspect.stack()[1][3]} ')
        if self.cols != other.cols or self.rows != other.rows:
            raise ValueError(f'Размеры матриц в операции {inspect.stack()[1][3]} не совпадают')


    def __lt__(self, other) -> bool:
        self._matrix_validate(other)
        self._size_validate(other)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.m[i][j] >= other.m[i][j]:
                    return False
        return True


    def __ge__(self, other) -> bool:
        return not self.__lt__(other)


    def __gt__(self, other) -> bool:
        self._matrix_validate(other)
        self._size_validate(other)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.m[i][j] <= other.m[i][j]:
                    return False
        return True


    def __le__(self, other) -> bool:
        return not self.__gt__(other)


    def __eq__(self, other) -> bool:
        try:
            self._matrix_validate(other)
            self._size_validate(other)
        except Exception:
            return False

        for i in range(self.rows):
            for j in range(self.cols):
                if self.m[i][j] != other.m[i][j]:
                    return False
        return True


    def __ne__(self, other) -> bool:
        return not self.__eq__(other)


    def __add__(self, other):
        self._matrix_validate(other)
        self._size_validate(other)
        result = []
        for i in range(self.rows):
            result.append([])
            for j in range(self.cols):
                result[i].append(self.m[i][j] + other.m[i][j])
        return Matrix(result)


    def transpose(self):
        return Matrix(np.array(self.m).transpose())


    def transpose2(self):
        return Matrix([list(row) for row in zip(*self.m)])

    def __rmul__(self, other):
        self._matrix_validate(other)
        if self.cols == other.rows:
            result = [[sum(a * b for a, b in zip(self_col, other_row))
                        for self_col in zip(*self.m)]
                        for other_row in other.m]
            return Matrix(result)
        else:
            raise ValueError('Некорректные размеры матриц в операции __rmul__')

    def __mul__(self, other):
        self._matrix_validate(other)
        if self.rows == other.cols:
            result = [[sum(a * b for a, b in zip(self_row, other_col))
                        for other_col in zip(*other.m)]
                        for self_row in self.m]
            return Matrix(result)
        else:
            raise ValueError('Некорректные размеры матриц в операции __mul__')

    '''
    def __mul__(self, other):
        self._matrix_validate(other)
        return Matrix(np.dot(self.m, other.m))

    '''

if __name__ == "__main__":
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m3 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    print(f"m1:\n{m1}")
    print(f"{m1=}")
    print(f"{m2=}")
    print(f"{m3=}")
    print(f"m1 == m2: {m1 == m2}")
    print(f"m1 == m3: {m1 == m3}")
    print(f"m1 != m2: {m1 != m2}")
    print(f"m1 != m3: {m1 != m3}")
    print(f"m1 < m2: {m1 < m2}")
    print(f"m1 <= m2: {m1 <= m2}")
    print(f"m1 > m2: {m1 > m2}")
    print(f"m1 >= m2: {m1 >= m2}")
    print(f'\nm1 + m2:\n{m1 + m2}')
    print(f'\nm1 * m2:\n{m1 * m2}')

    m4 = Matrix([[1, 2], [4, 5], [7, 8]])
    m5 = Matrix([[1, 2, 3], [4, 5, 6]])
    print(f'\nm4:\n{m4}')
    print(f'\nm4t:\n{m4.transpose()}')
    print(f'\nm5:\n{m5}')
    print(f'\nm5t2:\n{m5.transpose2()}')
    print(f'\nm4 * m5:\n{m4 * m5}')
    print(f'\nm5 * m4:\n{m5 * m4}')

