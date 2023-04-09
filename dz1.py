'''
Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата.
'''
from random import randint

def int_to_hex(num):
    tmp_num = num
    symbol = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hex_num = "";
    while tmp_num != 0:
        hex_num = symbol[tmp_num % 16] + hex_num
        tmp_num = tmp_num // 16
    hex_num = "0x" + hex_num
    print(f'{num} -> {hex_num}')

if __name__ == "__main__":
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    int_to_hex(num)
    print(f'{num} -> {hex(num).upper()}')


