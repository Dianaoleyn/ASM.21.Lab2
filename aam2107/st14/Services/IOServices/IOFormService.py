from flask import render_template
from Services.Abstracts.IOBaseService import IOBaseService


class IOFormService(IOBaseService):

    def __init__(self, request):
        self.request = request

    def input(self, obj):
        """Ввод"""
        for key, val in obj.__dict__.items():
            obj.__dict__[key] = self.__parse_data(self.request.form, key, val)

    def output(self, obj):
        """Вывод"""
        class_name = type(obj).__name__
        return render_template('form.tpl', stud=obj, modelName=class_name)

    def __parse_data(self, form, key, val):
        """Приватный метод парсинга значений из формы"""
        if isinstance(val, int):
            return int(form.get(str(key)))
        elif isinstance(val, float):
            return float(form.get(str(key)))
        else:
            return form.get(str(key))
