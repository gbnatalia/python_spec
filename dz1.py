'''
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''
import sys
from datetime import datetime

def leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def check_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        else:
            if 1 <= day <= 28 + leap_year(year):
                return True
    return False

def test_check_date(check_date:str, result:bool) ->bool:
    try:
        res = bool(datetime.strptime(check_date, '%d.%m.%Y'))
    except ValueError:
        res = False
    return res == result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_str = sys.argv[1]
        if check_date(test_str) == False:
            print(f"Ошибочный формат даты - {test_str}.")
        else:
            print(f"Дата {test_str} корректна.")
    else:
        print("Вы забыли ввести дату!")


