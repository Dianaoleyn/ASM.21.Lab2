from flask import request, render_template
from developer import Developer
from team_leader import TeamLeader


class HtmlStrategy:
    @staticmethod
    def home():
        return render_template('index.html')

    @staticmethod
    def message(message):
        return render_template('message.html', message=message)

    @staticmethod
    def add():
        return render_template('add.html')

    @staticmethod
    def dump(array):
        return render_template('list.html', array=array)

    @staticmethod
    def load():
        name = request.form['name']
        program_language = request.form['programLanguage']
        salary = request.form['salary']

        if request.form.get('isTeamlead'):
            annual_bonus = request.form['annualBonus']
            return [TeamLeader(name, program_language, salary, annual_bonus)]
        else:
            return [Developer(name, program_language, salary)]

