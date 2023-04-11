'''
Создайте словарь со списком вещей для похода в качестве ключа и
их массой в качестве значения.
Определить какие вещи влезут в рюкзак передав его максимальную грузоподъемность.
Достаточно вернуть один допустимый вариант.
* Все допустимые варианты коплектации рюкзака
'''

def find_combinations(items, max_weight):

    combos = [[]]
    for item, weight in items.items():
        new_combos = []
        for combo in combos:
            if sum([items[i] for i in combo]) + weight <= max_weight:
                new_combos.append(combo + [item])
        combos.extend(new_combos)
    return combos[1:]


if __name__ == "__main__":

    items = {"спальник": 2.5, "палатка": 3, "горелка": 1, "котелок": 0.8, "тушенка":0.5, "гречка": 1}
    max_weight = 5

    combinations = find_combinations(items, max_weight)
    for i, combo in enumerate(combinations):
        print(f"Вариант {i + 1}: {combo}")
