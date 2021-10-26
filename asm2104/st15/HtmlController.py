from flask import render_template, request

from Console import Console
from administrator import Administrator
from salesman import Salesman
from file import File


class HtmlController:
    def getMenu(self, item, employees):
        return render_template("menu.html", employees=employees)

    def getEmployees(self):
        return self.load()

    def changeStrategy(self):
        classes = [
            {'text': 'Файл', 'class': File},
            {'text': 'Консоль', 'class': Console},
        ]

        return render_template('changeStrategy.html', classes=classes)

    def showEmployees(self, employees):
        return render_template('list.html', employees=employees)

    def load(self):
        if request.form.get('stake'):
            st = Administrator(request.form.get('name'), request.form.get('salary'), request.form.get('stake'),
                               request.form.get('level'))
        else:
            st = Salesman(request.form.get('name'), request.form.get('salary'), request.form.get('stake'))
        return [st]
