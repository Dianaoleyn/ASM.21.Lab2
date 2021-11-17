import pickle

from flask import request

from aam2107.st14.Models.MainStudent import MainStudent
from aam2107.st14.Models.Student import Student
from aam2107.st14.Services.Abstracts.BaseContainer import BaseContainer

FILE_NAME = "container.db"


class ContainerPickle(BaseContainer):
    def __init__(self):
        try:
            self.load_from_file()
        except:
            self.all = {}
            self.maxid = 0

# Работа с файлом
    def store_to_file(self):
        """Запись в файл"""
        with open(FILE_NAME, 'wb') as file:
            pickle.dump((self.maxid, self.all), file)

    def load_from_file(self):
        """Чтение из файла"""
        with open(FILE_NAME, 'rb') as file:
            (self.maxid, self.all) = pickle.load(file)

    def clear_file(self) -> None:
        """Очистить файл"""
        with open(FILE_NAME, 'wb') as file:
            pickle.dump("", file)

# Работа с локальной коллекцией
    def get_by_id(self, id):
        """Получить студента по id"""
        return self.all[id]

    def get_all(self):
        """Получить всех студентов"""
        for (id, student) in self.all.items():
            yield student

    def get_ordinary_students(self):
        """Получить всех простых студентов"""
        for (id, student) in self.all.items():
            if type(student).__name__ is "Student":
                yield student

    def get_main_students(self):
        """Получить всех старост"""
        for (id, student) in self.all.items():
            if type(student).__name__ is "MainStudent":
                yield student

    def add(self, student):
        """Добавить учащегося"""
        if student.id <= 0:
            self.maxid += 1
            student.id = self.maxid
            self.all[student.id] = student
        self.store_to_file()

    def update(self, student):
        """Обновить информацию об учащемся"""
        self.all[student.id] = student
        self.store_to_file()

    def delete_by_id(self, id):
        """Удалить учащегося по id"""
        del self.all[id]
        self.store_to_file()

    def get_model(self):
        """Получить объект студента или старосты в зависимости от запроса"""
        if request.form.get('email') is not None:
            return MainStudent()
        else:
            return Student()
