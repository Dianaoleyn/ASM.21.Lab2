from Services.Abstracts.IOBaseService import IOBaseService


class IOConsoleService(IOBaseService):

    __description = {'first_name': 'Имя', 'middle_name': 'Отчество', 'last_name': 'Фамилия',
                     'age': 'Возраст', 'average_score': 'Средний балл', 'id': 'ID',
                     'email': 'Почта группы'}

    def input(self, obj):
        """Ввод свойств объекта"""
        for key, val in obj.__dict__.items():
            if key == 'id':
                continue
            input_value = input(f"{self.__description[key]}: ")
            obj.__dict__[key] = input_value

    def output(self, obj):
        """Вывод свойств объекта"""
        for key, val in obj.__dict__.items():
            print(self.__description[key], val)
