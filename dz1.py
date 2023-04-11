''''
Дан список с повторяющимися элементами. Вернуть список с дублирующими элементами.
В результирующем списке не должно быть дубликатов
'''
def get_clear_list(src):

    # список уникальных элементов
    unicum_src = list(set(src))

    # формируем список повторов
    repeat_lst = src.copy()
    for el in unicum_src:
        repeat_lst.remove(el)
    repeat_lst = list(set(repeat_lst))

    # формируем список из элементов src без повторов в порядке их следования в исх.списке
    dst = [el for el in src if el not in repeat_lst]

    return dst, repeat_lst


if __name__== "__main__":
    src_list = [2, 3, 6, 2, 9, 4, 2, 7, 2, 3, 6, 9, 0]
    print("Исходный список", src_list)
    dst_list, dbl_list = get_clear_list(src_list)
    print("Список без дубликатов", dst_list)
    print("Список дубликатов", dbl_list)