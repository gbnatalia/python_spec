'''
Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму и *произведение дробей.
Для проверки своего кода используйте модуль fractions
'''

from fractions import Fraction as f

def frac_op(str1, str2):
    num1 = list(map(int, str1.split("/")))
    num2 = list(map(int, str2.split("/")))
    f_sum = "/".join((str(num1[0]*num2[1] + num2[0]*num1[1]), str(num1[1]*num2[1])))
    f_mult = "/".join((str(num1[0] * num2[0]), str(num1[1] * num2[1])))
    return f_sum, f_mult

def frac_op2(str1, str2):
    f_sum = str(f(str1) + f(str2))
    f_mult = str(f(str1) * f(str2))
    return f_sum, f_mult

if __name__=="__main__":
    a = "1/3"
    b = "2/7"

    res = frac_op("1/3", "2/7")
    print(f"{a}+{b}={res[0]}, {a}*{b}={res[1]}")

    res2 = frac_op2(a, b)
    print(f"{a}+{b}={res2[0]}, {a}*{b}={res2[1]}")
