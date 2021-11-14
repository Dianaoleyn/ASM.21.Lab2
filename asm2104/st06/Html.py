from flask import render_template, request

from Manager import Manager
from Player import Player
from Staff import Staff


class Html:

    @staticmethod
    def dump(members):
        return render_template('show.html', members=members)

    @staticmethod
    def load():
        if request.form.get('position'):
            m = Player(1, 'Player', request.form.get('name'), request.form.get('surname'), request.form.get('age'),
                       request.form.get('position'))
        elif request.form.get('role'):
            m = Manager(1, 'Manager', request.form.get('name'), request.form.get('surname'), request.form.get('age'),
                        request.form.get('role'))
        else:
            m = Staff(1, 'Staff', request.form.get('name'), request.form.get('surname'), request.form.get('age'),
                      request.form.get('function'))
        return m