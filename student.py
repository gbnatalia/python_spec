'''
Создайте класс студента.
- Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
- Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
- Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых.
'''
import csv

from name_description import NameDescriptor
from subjects import SubjectsInfo


class Student:

    _name = NameDescriptor()
    _surname = NameDescriptor()
    _patronymic = NameDescriptor()
    _subjests = SubjectsInfo((2, 5), (0, 100))


    def __init__(self, surname: str, name: str, patronymic: str) -> None:
        self._name = name
        self._surname = surname
        self._patronymic = patronymic


    def __str__(self):
        return f"Студент - {self._surname} {self._name} {self._patronymic},\n"\
                f"Cредняя оценка - {self.average_marks},\n"\
                f"Cредний балл - {self.average_balls}"


    def update_subjects_info(self, subjects_info: list[tuple]) -> None:
        try:
            for subject_info in subjects_info:
                self._subjests.subjects = subject_info
        except Exception as e:
            raise(e)


    def print_attestat(self):
        print("--------------------------------------------------")
        print(f": {'Предмет':<25} : {'Оценка':^7} : {'Балл':^8} :")
        print("--------------------------------------------------")
        for key, value in self._subjests.subjects.items():
            print(f": {key:^25} : {value[0]:^7} : {value[1]:^8} :")
        print("--------------------------------------------------")


    @property
    def average_marks(self):
        sum_mark = 0
        for mark, ball in self._subjests.subjects.values():
            sum_mark += mark
        return int(sum_mark / len(self._subjests.subjects))


    @property
    def average_balls(self):
        sum_ball = 0
        for mark, ball in self._subjests.subjects.values():
            sum_ball += ball
        return int(sum_ball / len(self._subjests.subjects))


if __name__ == "__main__":

    def create_subjects_csv():
        with open('subjects.csv', 'w', encoding='utf-8') as subjects_file:
            writer = csv.writer(subjects_file, delimiter=",", lineterminator="\r")
            writer.writerow(["дискретная математика", 2, 0])
            writer.writerow(["математический анализ", 2, 0])
            writer.writerow(["английский", 2, 0])
            writer.writerow(["физическая подготовка", 2, 0])
            writer.writerow(["физика", 2, 0])
            writer.writerow(["история", 2, 0])

   # создание файла предметов/оценок/баллов
   # create_subjects_csv()

    #s = Student("иванов", 1, "123Иванович")
    s = Student("Иванов", "Иван", "Иванович")
    print(s)
    s.print_attestat()

    new_data = [
            ("дискретная математика", 5, 100),
            ("математический анализ", 4, 80),
            ("английский", 3, 50),
            ("физическая подготовка", 4, 75),
            ("физика", 5, 90),
            ("история", 5, 95)
        ]
    s.update_subjects_info(new_data)
    print(s)
    s.print_attestat()

    try:
        new_data2 = [
            ("дискретная математика", 6, 20),
            ("математический анализ", 4, 180),
            ("английский", 3, 50),
            ("физическая подготовка", 4, 75),
            ("физика", 5, 90),
            ("история", 5, 95)
            ]
        s.update_subjects_info(new_data2)
        print(s)
        s.print_attestat()
    except Exception as e:
        print(e)
