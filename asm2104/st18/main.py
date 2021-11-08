from flask import Flask, render_template, request, Markup
app = Flask(__name__)

if __name__ == '__main__':
    from group import group
else:
    from .group import group


from allCards import allCards
from storageStrategy import Pickle

from student import student
from groupLeader import groupLeader
from teacher import teacher
from proforg import proforg
from dean import dean
from employe import employe

from actionStrategy import Web

cont=allCards()

@app.route("/")
def main():
    return render_template('main.html')


def show(type=None):
    try:
        cont.load(Pickle)
    except:
        pass

    content = ''
    if type is None:
        for member in cont.users:
            content += member.output(Web)
            content += '<br>'
    else:
        for member in cont.users:
            if member.type==type:
                content += member.output(Web)
                content += '<br>'

    return render_template('show.html', context={'content': Markup(content)})


@app.route('/showall')
def showall():
    return show()

@app.route('/showstudent')
def showstudent():
    return show('student')

@app.route('/showemployes')
def showemployes():
    return show('employe')


def add(Class, action):
    # print(itemClass().__dict__)

    attribs_html=''
    for attr in Class().__dict__.keys():
        if attr!='type' and attr!='id' and attr!='position':
            attribs_html+=f'<label>{attr}</label><br>' \
                          f'<input id="{attr}" name="{attr}"><br><br>'

    return render_template('add.html', context={'attribs': Markup(attribs_html), 'action':action})

@app.route('/addstudent')
def addstudent():
    return add(student, 'add_student')

@app.route('/addemploye')
def addemploye():
    return add(employe, 'add_employe')

@app.route('/addgroupleader')
def addgroupleader():
    return add(groupLeader, 'add_groupleader')

@app.route('/addproforg')
def addproforg():
    return add(proforg, 'add_proforg')

@app.route('/addteacher')
def addteacher():
    return add(teacher, 'add_teacher')

@app.route('/adddean')
def adddean():
    return add(dean, 'add_dean')


def append(Class, type):
    try:
        cont.load(Pickle)
    except:pass

    obj=Class(type=type)
    obj.input(Web)
    cont.add_member(obj)
    cont.store(Pickle)

@app.route('/add_student', methods=['POST'])
def add_student():
    append(student, 'student')
    return 'Succes'

@app.route('/add_employe', methods=["POST"])
def add_employe():
    append(employe, 'employe')
    return 'Succes'

@app.route('/add_groupleader', methods=['POST'])
def add_groupleader():
    append(groupLeader, 'student')
    return 'Succes'

@app.route('/add_proforg', methods=['POST'])
def add_proforg():
    append(proforg, 'student')
    return 'Succes'

@app.route('/add_teacher', methods=['POST'])
def add_teacher():
    append(teacher, 'employe')
    return 'Succes'

@app.route('/add_dean', methods=['POST'])
def add_dean():
    append(dean, 'employe')
    return 'Succes'


@app.route('/search', methods=['GET'])
def search():
    try:
        cont.load(Pickle)
    except:pass

    find=cont.get_member(int(request.args['param']))
    if find is not None:
        content=find.output(Web)
        return render_template('show.html', context={'content': Markup(content)})
    else:
        return 'No results'

@app.route('/clear')
def clear():
    try:
        cont.clr()
        cont.store(Pickle)
        return 'Success'
    except: return 'Error'






if __name__ == "__main__":
    # add(student, 'student')
    app.run(debug=True)


