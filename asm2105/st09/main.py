from flask import Flask, render_template, request, redirect, g

from asm2105.st09.group import Group
from asm2105.st09.member import Member

app = Flask(__name__)


def getGroup():
    if 'group' not in g:
        g.group = Group()
        g.group.loadGroup()
    return g.group


student_types = [
    {'name': 'Студент', 'value': 'student'},
    {'name': 'Староста', 'value': 'groupLeader'}
]


@app.route('/')
def index():
    params = {'route': '/api/group/name', 'type': 'POST'}
    return render_template('index.html', params=params)


@app.route('/group')
def allStudents():
    return render_template('group.html', group=getGroup())


@app.route('/group/edit/<int:id>')
def edit(id):
    member = getGroup().getMemberById(id)
    return render_template(
        '/edit.html',
        params={'route': '/api/student/edit/' + str(member.id), 'type': 'POST'},
        member=member,
        items=student_types
    )


@app.route('/group/add')
def add():
    return render_template(
        'add.html',
        params={'route': '/api/student/add', 'type': 'POST'},
        member=Member(),
        items=student_types
    )


@app.route('/api/group/name', methods=['POST'])
def setGroupName():
    name = request.form['name']
    group = getGroup()
    group.clearStudents()
    group.name = name

    return redirect('/group')


@app.route('/api/group/load')
def loadGroup():
    return redirect('/group')


@app.route('/api/student/edit/<int:id>', methods=['POST'])
def editStudent(id):
    getGroup().editStudent(id)
    return redirect('/group')


@app.route('/api/student/add', methods=['POST'])
def addStudent():
    getGroup().addStudent()
    return redirect('/group')


@app.route('/api/student/delete/<int:id>')
def deleteStudent(id):
    getGroup().deleteStudent(id)
    return redirect('/group')


@app.teardown_appcontext
def writeFile(ctx):
    group = getGroup()
    if group.name != '':
        getGroup().saveGroup()


if __name__ == '__main__':
    app.run(debug=True)
