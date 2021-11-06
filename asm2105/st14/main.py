from flask import Flask, render_template, Markup, request
app = Flask(__name__)

if __name__ == '__main__':
    from group import group
else:
    from .group import group

from model.listEntry import Types

from model.school import school
from strategy.Storage import Pickle


from model.student import student
from model.worker import worker
from model.director import director
from model.teacher import teacher
from model.starosta import starosta
from strategy.Interaction import BrowserInteraction

import json

SCHOOL=school(Pickle)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/show')
def show_page():
    return render_template('show.html')

@app.route('/show_students')
def show_students():
    SCHOOL.load()
    content=''
    for item in SCHOOL.list.values():
        if item.type==Types.student:
            content+=item.Out()
            content+='<br>'

    return render_template('items.html', context={'content': Markup(content), 'type': 'Ученики'})

@app.route('/show_starostas')
def show_starostas():
    SCHOOL.load()
    content=''
    for item in SCHOOL.list.values():
        if item.type==Types.starosta:
            content+=item.Out()
            content+='<br>'

    return render_template('items.html', context={'content': Markup(content), 'type': 'Старосты'})

@app.route('/show_workers')
def show_workers():
    SCHOOL.load()
    content=''
    for item in SCHOOL.list.values():
        if item.type==Types.worker:
            content+=item.Out()
            content+='<br>'

    return render_template('items.html', context={'content': Markup(content), 'type': 'Сотрудники'})


@app.route('/show_teachers')
def show_teachers():
    SCHOOL.load()
    content=''
    for item in SCHOOL.list.values():
        if item.type==Types.teacher:
            content+=item.Out()
            content+='<br>'

    return render_template('items.html', context={'content': Markup(content), 'type': 'Учителя'})


@app.route('/show_directors')
def show_directors():
    SCHOOL.load()
    content=''
    for item in SCHOOL.list.values():
        if item.type==Types.director:
            content+=item.Out()
            content+='<br>'

    return render_template('items.html', context={'content': Markup(content), 'type': 'Директоры'})

@app.route('/show_all')
def show_all():
    SCHOOL.load()
    content=''
    for item in SCHOOL.list.values():
        content+=item.Out()
        content+='<br>'

    return render_template('items.html', context={'content': Markup(content), 'type': 'Все'})

@app.route('/add')
def add_page():
    return render_template('add.html')

@app.route('/add_student')
def add_student():
    return render_template('add_pages/add_student.html')

@app.route('/add_worker')
def add_worker():
    return render_template('add_pages/add_worker.html')

@app.route('/add_starosta')
def add_starosta():
    return render_template('add_pages/add_starosta.html')

@app.route('/add_teacher')
def add_teacher():
    return render_template('add_pages/add_teacher.html')

@app.route('/add_director')
def add_director():
    return render_template('add_pages/add_director.html')

@app.route('/append_student', methods=['POST'])
def append_student():
    SCHOOL.load()
    try:
        obj=student(BrowserInteraction)
        obj.In()
        SCHOOL.add(obj)
        SCHOOL.save()
        return 'Успех!'
    except:
        return 'Ошибка'

@app.route('/append_worker', methods=['POST'])
def append_worker():
    SCHOOL.load()
    try:
        obj=worker(BrowserInteraction)
        obj.In()
        SCHOOL.add(obj)
        SCHOOL.save()
        return 'Успех!'
    except:
        return 'Ошибка'

@app.route('/append_starosta', methods=['POST'])
def append_starosta():
    SCHOOL.load()
    try:
        obj=starosta(BrowserInteraction)
        obj.In()
        SCHOOL.add(obj)
        SCHOOL.save()
        return 'Успех!'
    except:
        return 'Ошибка'

@app.route('/append_director', methods=['POST'])
def append_director():
    SCHOOL.load()
    try:
        obj=director(BrowserInteraction)
        obj.In()
        SCHOOL.add(obj)
        SCHOOL.save()
        return 'Успех!'
    except:
        return 'Ошибка'

@app.route('/append_teacher', methods=['POST'])
def append_teacher():
    SCHOOL.load()
    try:
        obj=teacher(BrowserInteraction)
        obj.In()
        SCHOOL.add(obj)
        SCHOOL.save()
        return 'Успех!'
    except:
        return 'Ошибка'

@app.route('/clear')
def clear():
    SCHOOL.load()
    try:
        SCHOOL.clear()
        SCHOOL.save()
        return 'Успех!'
    except:
        return 'Ошибка'

@app.route('/search', methods=['GET'])
def search():
    SCHOOL.load()
    item=SCHOOL.search(request.args['param'])
    if item is None:
        return 'Не найдено'
    else:
        return str(item)


if __name__ == "__main__":
    app.run(debug=True)
