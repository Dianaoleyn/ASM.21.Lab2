from flask import Flask, render_template, redirect, g, request
from asm2105.st07.group import Group
from asm2105.st07.groupleader import GroupLeader
from asm2105.st07.storage import LocalStorage
from asm2105.st07.strategy import WebStrategy
from asm2105.st07.student import Student

app = Flask(__name__)

def getGroup():
    if 'group' not in g:
        g.group = Group(WebStrategy, LocalStorage)
        g.group.load()
    return g.group


@app.route('/')
def index():
    lst = list(map(lambda x: x.get(), getGroup().group_members))
    return render_template('index.html', items=lst)


@app.route('/add')
def add():
    types = [
        {'key': 'student', 'value': 'Студент'},
        {'key': 'groupLeader', 'value': 'Староста'}
    ]
    return render_template('add.html', items=types)


@app.route('/api/add', methods=['POST'])
def add_student():
    type = request.form['type']
    student = Student(WebStrategy) if type == 'student' else GroupLeader(WebStrategy)
    getGroup().add(student)
    return redirect('/')


@app.route('/api/clear')
def delete_students():
    getGroup().clear()
    return redirect('/')


@app.teardown_appcontext
def save(ctx):
    getGroup().save()


if __name__ == '__main__':
    app.run(debug=True)
