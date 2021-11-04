from flask import Flask, url_for, request, render_template, Markup, jsonify

app = Flask(__name__)

from objects.rgu import rgu
from strategies.storage import PickleStorage

from objects.item import item
from objects.student import student
from objects.worker import worker
from objects.zavkaf import zavkaf
from objects.starosta import starosta
from strategies.strategy import WebStrategy

import json

RGU=rgu(PickleStorage)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/show')
def show():
    return render_template('show.html')

@app.route('/showall')
def show_all():
    RGU.load()
    text = ''
    for member in RGU.members.values():
        print(member)
        text += member.get()
        text += '<br>'

    return render_template('members.html', context={'content': Markup(text), 'type': 'все'})

@app.route('/showstudents')
def show_st():
    RGU.load()
    text = ''
    for member in RGU.members.values():
        if member.type=='student':
            text += member.get()
            text += '<br>'

    return render_template('members.html', context={'content': Markup(text), 'type': 'Студенты'})


@app.route('/showworkers')
def show_wr():
    RGU.load()
    text = ''
    for member in RGU.members.values():
        if member.type=='worker':
            text += member.get()
            text += '<br>'

    return render_template('members.html', context={'content': Markup(text), 'type': 'Служащие'})


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/gettypeattr')
def get_attribs():
    # print(request.args['type'])
    type=request.args['type']
    attribs=[]

    if type=='student':
        obj=student(WebStrategy)
    elif type=='worker':
        obj=worker(WebStrategy)
    elif type=='zavkaf':
        obj=zavkaf(WebStrategy)
    elif type=='starosta':
        obj=starosta(WebStrategy)

    for attrib in obj.__dict__.keys():
        if attrib != 'id' and attrib != 'strategy' and attrib!='type':
            attribs.append(attrib)

    return json.dumps(attribs)


@app.route('/addmember', methods=['POST'])
def add_member():
    data = request.get_json()
    type = data['type']

    if type == 'student':
        obj = student(WebStrategy)
    elif type == 'worker':
        obj = worker(WebStrategy)
    elif type == 'zavkaf':
        obj = zavkaf(WebStrategy)
    elif type == 'starosta':
        obj = starosta(WebStrategy)

    obj.set()
    RGU.append(obj)
    RGU.save()
    return 'Успешно'

@app.route('/clear')
def clear():
    RGU.clear()
    RGU.save()
    return render_template('clear.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/searchid')
def get_from_search():
    print(request.args)
    RGU.load()
    member=RGU.search_by_id(int(request.args['id']))
    if member is not None:
        return member.get()
    else: return '0'


if __name__ == '__main__':
    app.run(debug=True)

