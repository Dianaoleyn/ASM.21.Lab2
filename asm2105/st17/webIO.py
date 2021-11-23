from flask import render_template, request
from student import Student
from headman import Headman


class WebIO:
    @staticmethod
    def output(array):
        return render_template('group.html', array=array)

    @staticmethod
    def input(id=None):
        name = request.form.get('name')
        surname = request.form.get('surname')
        average_score = request.form.get('average_score')
        grant = request.form.get('grant')
        if grant:
            return Headman(id, name, surname, average_score, grant)
        else:
            return Student(id, name, surname, average_score)

