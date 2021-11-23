from flask import request, render_template

from Models.MainStudent import MainStudent
from Models.Student import Student
from Services.Container import ContainerPickle
from Services.IOServices.IOFormService import IOFormService


class WebService:

    def __init__(self):
        self.container = ContainerPickle()
        self.io_base_service = IOFormService(request)

    def show_student_form(self):
        """Получить форму для студента"""
        return self.io_base_service.output(Student())

    def show_main_student_form(self):
        """Получить форму для старосты"""
        return self.io_base_service.output(MainStudent())

    def show_form(self, id):
        """Получить форму студента по id"""
        return self.io_base_service.output(self.container.get_by_id(id))

    def show_all(self):
        """Показать всех учащихся"""
        return render_template('catalog.tpl', students=self.container.get_ordinary_students(),
                               mainStudents=self.container.get_main_students())

    def add(self):
        """Добавить учащегося"""
        student = self.container.get_model()
        self.io_base_service.input(student)
        self.container.add(student)
        return self.show_all()

    def update(self):
        """Обновить информацию об учащемся"""
        student = self.container.get_by_id(int(request.form.get('id')))
        self.io_base_service.input(student)
        self.container.update(student)
        return self.show_all()

    def delete(self, id):
        """Удалить по id"""
        self.container.delete_by_id(id)
        return self.show_all()
