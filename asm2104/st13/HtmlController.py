from flask import render_template, request
from ConsoleIO import ConsoleIO
from student import Student
from headman import Headman
from fileIO import FileIO


class HtmlController:
    def getMenu(self, item):
        return render_template("menu.html")

    def addElement(self):
        return HtmlController.load()

    def changeStrategy(self):
        classes = [
            {'text': 'Файл', 'class': FileIO},
            {'text': 'Консоль', 'class': ConsoleIO},
            {'text': 'HTML', 'class': HtmlController}
        ]

        return render_template('changeStrategy.html', classes=classes)

    @staticmethod
    def dump(students):
        return render_template('list.html', students=students)

    @staticmethod
    def load():
        if request.form.get('additionalScholarship'):
            st = Headman(request.form.get('name'), request.form.get('surname'), request.form.get('averageRating'),
                         request.form.get('additionalScholarship'))
        else:
            st = Student(request.form.get('name'), request.form.get('surname'), request.form.get('averageRating'))
        return st
