from .ConsoleIO import WebIO
from flask import render_template


class Student:
    def __init__(self, id=0, name='', surname='', age='', io=WebIO()):
        self.__id = id
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__io = io

    def output(self):
        return self.__io.do_output(self)

    def input(self, form, maxid):
        self.__io.do_input(self, form, maxid)

    def form_print(self):
        return render_template('form.html', **self.__dict__)

    def __str__(self):
        return "Имя: {}, Фамилия: {}, Возраст: {}".format(
            self.__name, self.__surname, self.__age
        )
