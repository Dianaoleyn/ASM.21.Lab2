from flask import render_template, request

from asm2104.st06.Manager import Manager
from asm2104.st06.Player import Player
from asm2104.st06.Staff import Staff


class Html:

    @staticmethod
    def dump(members):
        return render_template('show_html.html', members=members)

    @staticmethod
    def load(list):
        if request.form.get('position'):
            m = Player(request.form.get('name'), request.form.get('surname'), request.form.get('age'),
                       request.form.get('position'))
        elif request.form.get('role'):
            m = Manager(request.form.get('name'), request.form.get('surname'), request.form.get('age'),
                        request.form.get('role'))
        else:
            m = Staff(request.form.get('name'), request.form.get('surname'), request.form.get('age'),
                      request.form.get('function'))
        return m