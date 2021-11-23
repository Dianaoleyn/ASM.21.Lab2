from flask import request, render_template
from player import Player
from captain import Captain


class HtmlIO:
    @staticmethod
    def dump(array):
        return render_template('fc.html', array=array)

    @staticmethod
    def load():
        name = request.form['name']
        number = request.form['number']
        nationality = request.form['nationality']
        age = request.form['age']

        if age:
            return [Captain(name, number, nationality, age)]
        else:
            return [Player(name, number, nationality)]
