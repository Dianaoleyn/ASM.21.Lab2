from flask import Flask, request, render_template, url_for, redirect
from ConsoleIO import ConsoleIO
from HtmlController import HtmlController
from fileIO import FileIO

app = Flask(__name__)

if __name__ == '__main__':
    from group import Group
else:
    from .group import Group

group = Group()
classes = [
    {'text': 'Файл', 'class': FileIO},
    {'text': 'Консоль', 'class': ConsoleIO},
    {'text': 'HTML', 'class': HtmlController}
]

@app.route("/")
def main():
    return group.getMenu()


@app.route("/add", methods=['GET'])
def getForm():
    return render_template('add.html')


@app.route("/add", methods=['POST'])
def add():
    group.addElement()
    redirect(url_for('main'))
    return group.getMenu()


@app.route("/clear", methods=['GET'])
def clear():
    group.clearList()
    redirect(url_for('main'))
    return group.getMenu()


@app.route("/changeStrategy", methods=['GET'])
def changeStrategy():
    return group.changeStrategy()


@app.route("/changeStrategy", methods=['POST'])
def changeStrategyResult():
    for i in classes:
        if i.get('text') == request.form.get('class'):
            group.strategy = i.get('class')
            break
    redirect(url_for('main'))
    return group.getMenu()


@app.route("/list", methods=['GET'])
def getStudents():
    dump = group.dump()
    if (dump is None):
        redirect(url_for('main'))
        return group.getMenu()
    return group.dump()


@app.route("/load", methods=['GET'])
def load():
    group.load()
    redirect(url_for('main'))
    return group.getMenu()


if __name__ == "__main__":
    app.run(app.run(debug=True))
