class NameDescriptor:
    '''
    Дескриптор для Имени, Фамилии, Отчества
    '''
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, name_property):        
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f"Параметр {self.param_name} должен быть строкой")
        if len(value) == 0:
            raise ValueError(f"Параметр {self.param_name} не должен иметь нулевую длину")
        if not value.isalpha():
            raise ValueError(f"Параметр {self.param_name} должен содержать только буквы")
        if value[0] != value[0].upper():
            raise ValueError(f"Первая буква параметра {self.param_name} должна быть заглавной")        