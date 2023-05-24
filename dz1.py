'''
1. Создайте класс-фабрику.
- Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
- Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.
'''


class Mammal:
    def __init__(self, type, age, paws):
        self.type, self.age, self.paws = type, age, paws

    def __str__(self):
        return f"Зверь: {self.type}, возраст: {self.age} лет/год(а), лапы: {self.paws}"


class Fish:
    def __init__(self, type, age, color):
        self.type, self.age, self.color = type, age, color

    def __str__(self):
        return f"Рыба: {self.type}, возраст: {self.age} лет/год(а), цвет: {self.color}"


class Bird:
    def __init__(self, type, age, feathers):
        self.type, self.age, self.feathers = type, age, feathers

    def __str__(self):
        return f"Птица: {self.type}, возраст: {self.age} лет/год(а, крылья: {self.feathers}"


class FabricaClass:
    __class_dict = {}

    def register_class(self, class_name, class_h):
        self.__class_dict[class_name] = class_h
        return self

    def get_instance(self, type_class, *args, **kwargs):
        if type_class in self.__class_dict.keys():
            return self.__class_dict[type_class](*args, **kwargs)
        else:
            print(f"Класс {type_class} не зарегистрирован!")
            return None


if __name__ == "__main__":
    fabr = FabricaClass()
    fabr.register_class("Mammal", Mammal).register_class("Fish", Fish).register_class("Bird", Bird)
    my_mammal = fabr.get_instance("Mammal", "Кошка", 5, "рыжая")
    my_fish = fabr.get_instance("Fish", "Гуппи", 22, "Красно-белая")
    my_bird = fabr.get_instance("Bird", "Ворона", 2, "Черная")
    print(my_mammal)
    print(my_fish)
    print(my_bird)

    fabr2 = FabricaClass()
    my_mammal2 = fabr2.get_instance("Mammal", "Собака", 15, "Черно-белая")
    print(my_mammal2)

    fabr3 = FabricaClass()
    my_mammal3 = fabr2.get_instance("MMM", "Собака", 15, "Черно-белая")
    print(my_mammal3)

