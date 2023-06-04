import inspect
from matrix_exception import *

class Matrix:


    def __init__(self, m):
        self.__list_list_validate(m)
        self.m = m
        self.rows = len(m)
        self.cols = len(m[0])


    def __list_list_validate(self, m):
        if m == None:
            raise MatrixTypeDataError(inspect.stack()[1][3], m)
        elif not isinstance(m, list):
            raise MatrixTypeDataError(inspect.stack()[1][3], m)
        elif not len(m):
            raise MatrixTypeDataError(inspect.stack()[1][3], m)
        elif not isinstance(m[0], list):
            raise MatrixTypeDataError(inspect.stack()[1][3], m)
        elif not len(m[0]):
            raise MatrixTypeDataError(inspect.stack()[1][3], m)


    def __matrix_validate(self, matr):
        if not isinstance(matr, Matrix):
            raise MatrixClassError


    def __matrix_add_sub_compare_size_validate(self, m1, m2):
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            raise MatrixSizeError(m1, m2, inspect.stack()[1][3])


    def __str__(self) -> str:
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.m])


    def __repr__(self) -> str:
        return f'"Matrix({self.m})"'


    def __lt__(self, other) -> bool:
        self.__matrix_validate(other)
        self.__matrix_add_sub_compare_size_validate(self.m, other.m)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.m[i][j] >= other.m[i][j]:
                    return False
        return True


    def __ge__(self, other) -> bool:
        return not self.__lt__(other)


    def __gt__(self, other) -> bool:
        self.__matrix_validate(other)
        self.__matrix_add_sub_compare_size_validate(self.m, other.m)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.m[i][j] <= other.m[i][j]:
                    return False
        return True


    def __le__(self, other) -> bool:
        return not self.__gt__(other)


    def __eq__(self, other) -> bool:
        self.__matrix_validate(other)
        self.__matrix_add_sub_compare_size_validate(self.m, other.m)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.m[i][j] != other.m[i][j]:
                    return False
        return True


    def __ne__(self, other) -> bool:
        return not self.__eq__(other)


    def __add__(self, other):
        self.__matrix_validate(other)
        self.__matrix_add_sub_compare_size_validate(self.m, other.m)
        result = []
        for i in range(self.rows):
            result.append([])
            for j in range(self.cols):
                result[i].append(self.m[i][j] + other.m[i][j])
        return Matrix(result)


    def transpose(self):
        return Matrix([list(row) for row in zip(*self.m)])


if __name__ == "__main__":

    '''
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m3 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    m4 = Matrix([[1, 2], [4, 5], [7, 8]])
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
    print(f'\nm4:\n{m4}')
    print(f'\nm4t:\n{m4.transpose()}')
    '''

    try:
        m1 = Matrix(None)
    except MatrixTypeDataError as e:
        print(e)

    try:
        m2 = Matrix([])
    except MatrixTypeDataError as e:
        print(e)

    try:
        m3 = Matrix([[1, 2], [2, 3]])
        m4 = Matrix([[1, 2], [2, 3], [3, 4]])
        m5 = m3 + m4
    except MatrixSizeError as e:
        print(e)

