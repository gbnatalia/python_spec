from dz6_packadge import *

print("Задание 1. Дополнение")
test_date = ["22.01.1971", "31.02.1971", "29.02.1971"]
for it in test_date:
    print(f"Результат теста функции (check_date) проверки даты {it} - {test_check_date(it, check_date(it))}")

print("\nЗадание 2")
arr1 = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 1)]
res1 = chess(arr1)
print("Исх.список", arr1, "- Результат - ", res1[0])
print("Список вариантов, когда ферзи бьют друг друга", res1[1])

arr2 = [(1, 2), (2, 3), (3, 4), (1, 5), (5, 2), (6, 7), (7, 8), (8, 1)]
res2 = chess(arr2)
print("Исх.список", arr2, "- Результат - ", res2[0])
print("Список вариантов, когда ферзи бьют друг друга", res2[1])

print("\nЗадание 3")
cnt_var = 4
while cnt_var:
    arr = get_variant()
    if chess(arr)[0] == True:
        print(arr)
        cnt_var -= 1
