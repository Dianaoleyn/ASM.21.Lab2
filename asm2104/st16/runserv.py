from flask import Flask, url_for, request, render_template, Markup, redirect


app = Flask(__name__)

from container import container
from sluzh import sluzh
from director import director
from teacher import teacher
from student import student
from starosta import starosta
from pickleStrategy import PickleStorage
from Web import Web


c=container()

@app.route('/')
def base():
    try:
        c.load(PickleStorage)
    except: pass

    context=[Markup(member.output(Web)) for member in c.elements]

    return render_template('main.html', context={'elements':context})

@app.route('/add_element')
def add_element():
    return render_template('add_element_form.html')

@app.route('/add-new', methods=['POST'])
def add_new():
    print(request.form)
    if request.form['name'] is None or request.form['name']=='' or request.form['age'] is None or request.form['age']=='':
        return 'Invalid input form'

    if request.form['group'] is not None and request.form['group']!='':
        if request.form['email'] is not None and request.form['email']!='':
            item=starosta()
        else:
            item=student()
    else:
        if request.form['predmet'] is not None and request.form['predmet']!='':
            item=teacher()
        elif request.form['phone'] is not None and request.form['phone']!='' and request.form['cabinet'] is not None and request.form['cabinet']!='':
            item=director()
        else:
            item=sluzh()

    item.input(Web)
    try:
        c.load(PickleStorage)
    except:pass
    c.add_member(item)
    c.store(PickleStorage)

    return redirect('/')

@app.route('/clear')
def clear():
    c.clr()
    c.store(PickleStorage)
    return redirect('/')

@app.route('/refactor/<int:id>', methods=['POST', 'GET'])
def refactor(id):
    try:
        c.load(PickleStorage)
    except:
        return "can't load file"
    element = c.get_member(int(id))

    if request.method=='GET':
        return render_template('refactor_element.html', context={'element':element})
    else:
        element.input(Web)
        c.store(PickleStorage)
        return redirect('/')

@app.route('/search')
def search():
    param=request.args['search-param']

    try:
        c.load(PickleStorage)
    except:
        return "can't load file"
    result=c.get_member(param)
    if type(result) is list:
        context = [Markup(member.output(Web)) for member in result]

    else:
        context=[Markup(result.output(Web))]
    return render_template('main.html', context={'elements': context})


if __name__ == '__main__':
    app.run(debug=True)
