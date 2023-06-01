import csv

class SubjectsInfo:

    _subjects = {}


    def __init__(self, range1, range2):
        self.range1 = range1
        self.range2 = range2
        self.my_dict = {}
        with open('subjects.csv', 'r', encoding='utf-8') as subjects_file:
            reader = csv.reader(subjects_file, delimiter=",")
            for row in reader:
                self._subjects[row[0]] = (int(row[1]), int(row[2]))


    @property
    def subjects(self):
        return self._subjects


    @subjects.setter
    def subjects(self, new_value):
        if len(new_value) != 3:
            raise ValueError(f"В качестве параметра ожидается кортеж из 3х элементов!")
        if new_value[0] in self._subjects.keys():
            mark = int(new_value[1])
            ball = int(new_value[2])
            if mark > self.range1[1] or mark < self.range1[0]:
                raise ValueError(f"Отметка {mark} вне допустимого диапазона {self.range1}")
            if ball > self.range2[1] or mark < self.range2[0]:
                raise ValueError(f"Баллы {ball} вне допустимого диапазона {self.range2}")
            self._subjects[new_value[0]] = (mark, ball)

