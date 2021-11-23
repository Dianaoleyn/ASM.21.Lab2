from file_storage import FileStorage
from webIO import WebIO
from flask import render_template


class Group:
    def __init__(self):
        self.__storage = FileStorage()
        self.__io = WebIO()

    def add_element_form(self):
        return render_template('form.html', student=None)

    def edit_element_form(self, id):
        return render_template('form.html', student=self.__storage.get_element(id))

    def add_element(self):
        self.__storage.add_element(self.__io.input())

    def edit_element(self, id):
        self.__storage.edit_element(self.__io.input(id))

    def delete_element(self, id):
        self.__storage.delete_element(id)

    def delete_all(self):
        self.__storage.delete_all_elements()

    def show_elements(self):
        return self.__io.output(self.__storage.get_all_elements())

    def save_all_elements(self):
        return self.__storage.dump()
