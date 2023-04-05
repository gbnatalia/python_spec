'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки.
Для генерации случайного числа используйте код: from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)
'''
from random import randint


def one_step(num):
    while True:
        try:
            my_num = int(input("Введите число в диапазоне от 0 до 1000: "))
            if my_num < 0 or my_num > 1000:
                raise Exception("Число вне допустимого диапазона")
            if my_num == num:
                print("Вы угадали!")
                return True
            elif my_num < num:
                print("Загаданное число больше введенного!")
            else:
                print("Загаданное число меньше введенного!")
            return False
        except:
            print("Вы ввели некорректное число!")


def game():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    CNT_STEP = 10

    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    step = CNT_STEP

    while step > 0:
        if one_step(num) == True:
            print("Игра завершена! Вы выиграли!")
            break
        step -= 1
    else:
        print("Игра завершена! Вы проиграли!")


def game_in_ten_step():
    CNT_STEP = 10
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    step = CNT_STEP
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    print(f"загадано число - {num}")
    min = LOWER_LIMIT
    max = UPPER_LIMIT

    while step > 0:
        my_num = min + (max - min) // 2
        print(f"==> мое число - {my_num}", end="")

        if my_num == num:
            print(f" - угадано в {CNT_STEP - step} ходов")
            break
        elif my_num > num:
            print(" - больше загаданного")
            max = my_num
        else:
            print(" - меньше загаданного")
            min = my_num

        step -= 1
    else:
        print(f"число не угадано")


if __name__ == "__main__":
    game_in_ten_step()
