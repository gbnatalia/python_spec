'''
1.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
'''
import logging

def treug(a, b, c):
    '''
    1. Проверяет образуют ли стороны a, b, c - треугольник (существует ли треугольник)
    2. Проверяет является ли треугольник разносторонним, равнобедренным или равносторонним.
    :param a: 1-ая предполагаемая сторона треуголника
    :param b: 2-ая предполагаемая сторона треуголника
    :param c: 3-ая предполагаемая сторона треуголника
    '''
    FORMAT = '{levelname:<8}: {asctime} : {name:<10} : {lineno:03d} : {funcName:<10} : {msg}'
    logging.basicConfig(
        filename='treug.log', filemode='a', encoding='utf-8',
        format=FORMAT, style='{', level=logging.INFO)
    my_log = logging.getLogger(__name__)
    my_log.info(f"Получены следующие значения сторон: {a}, {b}, {c}")

    if a + b > c and b + c > a and a + c > b:
        my_log.info("Треугольник существует")
        if a == b or a == c or b == c:
            my_log.info("Треугольник равнобедренный")
            if a == b and a == c and b == c:
                my_log.info("Треугольник равносторонний")
        else:
            my_log.info("Треугольник разносторонний")
    else:
        my_log.error("Треугольник не существует")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', metavar='a b c', type=int, nargs=3,
                        help='Введите стороны треугольника a, b, c через зарятую или пробел')
    args = parser.parse_args()
    treug(*args.numbers)

'''
    treug(1, 2, 3)
    treug(2, 2, 3)
    treug(2, 2, 2)
    treug(4, 2, 3)
'''