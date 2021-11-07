from flask import Flask, url_for, request, render_template, Markup
from Objects.RGU import RGU
from Strategies.Storage import PickleStorage

from Objects.Student import Student
from Objects.Staff import Staff
from Objects.Decan import Decan
from Objects.Starosta import Starosta


from Strategies.GetSet import WebGetSet


app = Flask(__name__)
rgu=RGU(PickleStorage)

@app.route('/')
def main():
    return render_template('main.html')

def show(itemclass=None):
    try:
        rgu.load()
    except:pass

    content = ''
    if itemclass is None:
        for member in rgu.members.values():
            content+=member.print()
            content+='<br><br>'
    else:
        for member in rgu.members.values():
            if isinstance(member, itemclass):
                content+=member.print()
                content+='<br><br>'

    return render_template('show.html', context={'content': Markup(content)})

@app.route('/showall')
def showAll():
    return show()

@app.route('/showstudent')
def showStudent():
    return show(Student)

@app.route('/showstarosta')
def showStarosta():
    return show(Starosta)

@app.route('/showstaff')
def showStaff():
    return show(Staff)

@app.route('/showdecan')
def showDecan():
    return show(Decan)


def add(itemClass,action):
    attribs_html=''
    for attr, name in itemClass.get_attribs().items():
        if attr!='strategy':
            attribs_html+=f'<label>{name}</label><br>' \
                          f'<input id="{attr}" name="{attr}"><br><br>'

    return render_template('add.html', context={'attribs': Markup(attribs_html), 'action':action})

@app.route('/addstudent')
def addStudent():
    return add(Student, '/appendstudent')

@app.route('/addstarosta')
def addStarosta():
    return add(Starosta, '/appendstarosta')

@app.route('/addstaff')
def addStaff():
    return add(Staff, '/appendstaff')

@app.route('/adddecan')
def addDirector():
    return add(Decan, '/appenddecan')


def append(itemClass):
    try:
        rgu.load()
    except:pass
    obj=itemClass(WebGetSet)
    obj.set()
    rgu.add_member(obj)
    rgu.save()


@app.route('/appendstudent', methods=['POST'])
def appendStudent():
    try:
        append(Student)
        return 'Успех'
    except:
        return 'Ошибка'

@app.route('/appendstarosta', methods=['POST'])
def appendStarosta():
    try:
        append(Starosta)
        return 'Успех'
    except:
        return 'Ошибка'

@app.route('/appendstaff', methods=['POST'])
def appendStaff():
    try:
        append(Staff)
        return 'Успех'
    except:
        return 'Ошибка'

@app.route('/appenddecan', methods=['POST'])
def appendDecan():
    try:
        append(Decan)
        return 'Успех'
    except:
        return 'Ошибка'

@app.route('/search', methods=['GET'])
def search():
    try:
        rgu.load()
    except:pass

    find=rgu.get_by_num(int(request.args['number']))
    if find is not None:
        content=find.print()
        return render_template('show.html', context={'content': Markup(content)})
    else:
        return 'Не найдено'

@app.route('/clear')
def clear():
    try:
        rgu.clear()
        rgu.save()
        return 'Успех'
    except: return 'Ошибка'

    # print(request.args['number'])







if __name__ == '__main__':
    app.run(debug=True)