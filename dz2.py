'''
 Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''
from pathlib import Path
import re


def is_valid_filename(filename):
    allowed_chars = " ._-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    regex = "^[" + allowed_chars + "]+$"
    match = re.match(regex, filename)
    if match:
        return True
    else:
        return False


def group_rename(path, name, range_name, count_num, src_ext, dst_ext):
    if not path.is_dir():
        print("Задан некорректный путь к файлам!")
        return

    if len(src_ext) == 0 or src_ext[0] != "." or len(dst_ext) == 0 or dst_ext[0] != ".":
        print("Задано некорректное расширение!")
        return

    if range_name[0] >= range_name[1] or range_name[0] < 0 or range_name[1] > len(name):
        print("Задан некорректный диапазон букв результирующего файла!")
        return

    if not is_valid_filename(name):
        print("Задана некорректная строка для имени файлов!")
        return

    index = 0
    for obj in Path(path).iterdir():
        if obj.is_file() and Path(obj).suffix == src_ext:
            index += 1
            Path(obj).rename(f"{path}/{name[range_name[0]:range_name[1]]}_{index:0{count_num}}{dst_ext}")


if __name__ == "__main__":
    group_rename(Path().cwd().parent / "FILES2", "my_result_file", [3, 14], 3, ".txt", ".md")
