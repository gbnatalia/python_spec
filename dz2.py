'''
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
'''


def generator_dict(names, rates, premiums):
    return {name: round(rate * float(premium[:-1]) / 100, 2) for name, rate, premium in zip(names, rates, premiums)}


if __name__ == "__main__":
    names = ["Паша", "Саша", "Миша"]
    rates = [100, 200, 300]
    premiums = ["10.0%", "10.25%", "10.5%"]
    print(generator_dict(names, rates, premiums))
