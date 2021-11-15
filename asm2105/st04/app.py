from operator import methodcaller

from flask import Flask, render_template, redirect, g

from asm2105.st04.group import Group

app = Flask(__name__)

def getGroup():
    if 'group' not in g:
        g.group = Group()
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
    params = {'route': '/api/add', 'type': 'POST'}
    return render_template('add.html', items=types, params=params)


@app.route('/api/add', methods=['POST'])
def add_student():
    getGroup().add()
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
