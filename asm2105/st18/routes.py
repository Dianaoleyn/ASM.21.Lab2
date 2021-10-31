from app import app
from flask import render_template, request, Markup
from strategys.interactive import BrowserInteractive
# from asm2105.st18.models.student import
# from app import univer
from models.university import university
from strategys.storage import PickleStorage
from models.student import student
from models.employe import employe
from models.proforg import proforg
from models.decan import decan
import json

@app.route("/")
def main():
    return render_template('main_page.html')

@app.route('/show_all')
def show_all():
    main_container=university(PickleStorage)
    content=''
    for item in main_container.items.values():
        content+=item.Print()
        content+='<br>'

    return render_template('all_items.html', context={'content': Markup(content), 'type': 'все'})

@app.route('/show_students')
def show_students():
    main_container=university(PickleStorage)
    content=''
    for item in main_container.items.values():
        if item.type=='student':
            content+=item.Print()
            content+='<br>'

    return render_template('all_items.html', context={'content': Markup(content), 'type': 'студенты'})

@app.route('/show_employes')
def show_employes():
    main_container=university(PickleStorage)
    content=''
    for item in main_container.items.values():
        if item.type=='employe':
            content+=item.Print()
            content+='<br>'

    return render_template('all_items.html', context={'content': Markup(content), 'type': 'служащие'})

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/getattribs')
def get_attribs():
    # print(request.args['type'])
    type=request.args['type']
    attribs=[]

    if type=='student':
        obj=student(BrowserInteractive)
    elif type=='employe':
        obj=employe(BrowserInteractive)
    elif type=='proforg':
        obj=proforg(BrowserInteractive)
    elif type=='decan':
        obj=decan(BrowserInteractive)

    for attrib in obj.__dict__.keys():
        if attrib != 'id' and attrib != 'interactive' and attrib!='type':
            attribs.append(attrib)

    return json.dumps(attribs)

@app.route('/add_item', methods=['POST'])
def add_item():
    try:
        data=json.loads(request.form['data'])
        print(request.form['data'])
        type = data['type']

        if type == 'student':
            obj = student(BrowserInteractive)
        elif type == 'employe':
            obj = employe(BrowserInteractive)
        elif type == 'proforg':
            obj = proforg(BrowserInteractive)
        elif type == 'decan':
            obj = decan(BrowserInteractive)

        obj.Enter()
        main_container = university(PickleStorage)
        main_container.addItem(obj)
        main_container.dump()
        return 'Успешно'
    except Exception as err:
        return f'Ошибка: {err}'

@app.route('/by_num')
def search_by_num():
    return render_template('search.html')

@app.route('/get_by_num')
def get_by_num():
    main_container = university(PickleStorage)
    item=main_container.get_by_number(request.args['id'])
    if item is None:
        return 'false'
    else:
        return item.Print()

@app.route('/clear', methods=['POST', 'GET'])
def clear():
    try:
        main_container = university(PickleStorage)
        main_container.clear()
        main_container.dump()
        return 'Успешно'
    except Exception as err:
        return f'Ошибка: {err}'


    # print(request.args['id'])

# @app.route('/test')
# def test():
#     BrowserInteractive().Enter('yo')

