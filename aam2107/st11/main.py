from flask import Flask, request, render_template, url_for, redirect

from Console import Console
from HtmlController import HtmlController
from file import File

app = Flask(__name__)

if __name__ == '__main__':
    from pharmacy import Pharmacy
else:
    from .pharmacy import Pharmacy

pharmacy = Pharmacy()
classes = [
    {'text': 'Файл', 'class': File},
    {'text': 'Консоль', 'class': Console},
    {'text': 'HTML', 'class': HtmlController}
]

@app.route("/")
def main():
    return pharmacy.getMenu()


@app.route("/add", methods=['GET'])
def getForm():
    return render_template('add.html')


@app.route("/add", methods=['POST'])
def add():
    pharmacy.addEmployee()
    redirect(url_for('main'))
    return pharmacy.getMenu()


@app.route("/clear", methods=['GET'])
def clear():
    pharmacy.clearEmployees()
    redirect(url_for('main'))
    return pharmacy.getMenu()


@app.route("/changeStrategy", methods=['GET'])
def changeStrategy():
    return pharmacy.changeStrategy()


@app.route("/changeStrategy", methods=['POST'])
def changeStrategyResult():
    for i in classes:
        if i.get('text') == request.form.get('class'):
            pharmacy.strategy = i.get('class')()
            break
    redirect(url_for('main'))
    return pharmacy.getMenu()


@app.route("/list", methods=['GET'])
def getStudents():
    dump = shop.showEmployees()
    if (dump is None):
        redirect(url_for('main'))
        return pharmacy.getMenu()
    return pharmacy.showEmployees()


@app.route("/load", methods=['GET'])
def load():
    pharmacy.getEmployees()
    redirect(url_for('main'))
    return pharmacy.getMenu()


if __name__ == "__main__":
    app.run(app.run(debug=True))
