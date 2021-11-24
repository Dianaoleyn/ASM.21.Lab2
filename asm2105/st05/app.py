from flask import Flask, render_template, redirect, g, request
from group import Group
from superdinosaur import SuperDinosaur
from storage import LocalStorage
from strategy import WebStrategy
from dinosaur import Dinosaur

app = Flask(__name__)

def getGroup():
    if 'group' not in g:
        g.group = Group(WebStrategy, LocalStorage)
        g.group.load()
    return g.group


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add')
def add():
    types = [
        {'key': 'dinosaur', 'value': 'Simple'},
        {'key': 'superDinosaur', 'value': 'Super'}
    ]
    return render_template('add.html', items=types)


@app.route('/api/add', methods=['POST'])
def add_student():
    type = request.form['type']
    dino = Dinosaur(WebStrategy) if type == 'dinosaur' else SuperDinosaur(WebStrategy)
    getGroup().add(dino)
    return redirect('/')

@app.route('/show')
def loadandshow():
    lst = list(map(lambda x: x.get(), getGroup().group_members))
    return render_template('index.html', items=lst)

@app.route('/delete')
def deleteone():
    return render_template('delete.html')

@app.route('/api/delete', methods=['GET','POST'])
def deleteObject():
    if request.method=='GET':
        return render_template('delete.html')
    else:
        getGroup().deleteObject(request.form['index'])
        return render_template('index.html')

@app.route('/api/clear')
def delete_students():
    getGroup().clear()
    return redirect('/')


@app.teardown_appcontext
def save(ctx):
    getGroup().save()


if __name__ == '__main__':
    app.run(debug=True)
