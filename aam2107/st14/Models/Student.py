from dataclasses import dataclass
from flask import render_template


@dataclass
class Student:
    first_name: str = ''
    middle_name: str = ''
    last_name: str = ''
    age: int = 0
    average_score: float = 0.0
    id: int = 0

    def set_form_data(self, form):
        """Записать объект в файл"""
        for key, val in self.__dict__.items():
            self.__dict__[key] = self.__parse_data(form, key, val)

    def get_form(self):
        """Показать форму для заполнения данных студента"""
        class_name = type(self).__name__
        return render_template('form.tpl', stud=self, modelName=class_name)

    def __str__(self) -> str:
        """Получить объект класса студента в строковом виде"""
        return f'\nФИО: {self.last_name} {self.first_name} {self.middle_name};\n' \
               f'Возраст: {self.age};\n' \
               f'Средний балл: {self.average_score}'

    def __parse_data(self, form, key, val):
        """Приватный метод парсинга значений из формы"""
        if isinstance(val, int):
            return int(form.get(str(key)))
        elif isinstance(val, float):
            return float(form.get(str(key)))
        else:
            return form.get(str(key))
