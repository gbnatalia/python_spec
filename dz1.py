'''
Напишите функцию для транспонирования матрицы
'''
import numpy as np

def my_transpose(m):
    trans_m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return trans_m

if __name__ == "__main__":
    m = [[2,1,5],[7,4,9]]
    print(m)
    trans_m = my_transpose(m)
    print(trans_m)

    print("==================")
    m2 = np.array(m)
    print(m2)
    trans_m2 = np.transpose(m2)
    print(trans_m2)
