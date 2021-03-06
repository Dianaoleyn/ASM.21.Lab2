from flask import render_template
from ConsoleIO import ConsoleIO, WebIO


class Employee:
    def __init__(self, id=0, name='', surname='', age='', salary='', io=WebIO()):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
        self.io = io

    def output(self):
        return self.io.do_output(self)

    def input(self, form, maxid):
        self.io.do_input(self, form, maxid)

    def form_print(self):
        return render_template('form.html', **self.__dict__)

    def __str__(self):
        return "Имя: {}, Фамилия: {}, Возраст: {}, Зарплата: {}".format(
            self.name, self.surname, self.age, self.salary
        )
