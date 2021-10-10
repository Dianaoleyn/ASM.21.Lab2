from flask import Flask, request, render_template, url_for, redirect

from Console import Console
from HtmlController import HtmlController
from file import File

app = Flask(__name__)

if __name__ == '__main__':
    from shop import Shop
else:
    from .shop import Shop

shop = Shop()
classes = [
    {'text': 'Файл', 'class': File},
    {'text': 'Консоль', 'class': Console},
    {'text': 'HTML', 'class': HtmlController}
]

@app.route("/")
def main():
    return shop.getMenu()


@app.route("/add", methods=['GET'])
def getForm():
    return render_template('add.html')


@app.route("/add", methods=['POST'])
def add():
    shop.addEmployee()
    redirect(url_for('main'))
    return shop.getMenu()


@app.route("/clear", methods=['GET'])
def clear():
    shop.clearEmployees()
    redirect(url_for('main'))
    return shop.getMenu()


@app.route("/changeStrategy", methods=['GET'])
def changeStrategy():
    return shop.changeStrategy()


@app.route("/changeStrategy", methods=['POST'])
def changeStrategyResult():
    for i in classes:
        if i.get('text') == request.form.get('class'):
            shop.strategy = i.get('class')()
            break
    redirect(url_for('main'))
    return shop.getMenu()


@app.route("/list", methods=['GET'])
def getStudents():
    dump = shop.showEmployees()
    if (dump is None):
        redirect(url_for('main'))
        return shop.getMenu()
    return shop.showEmployees()


@app.route("/load", methods=['GET'])
def load():
    shop.getEmployees()
    redirect(url_for('main'))
    return shop.getMenu()


if __name__ == "__main__":
    app.run(app.run(debug=True))
