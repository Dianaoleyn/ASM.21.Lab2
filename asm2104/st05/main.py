"""
Работа: Ерыгина Светлана АСМ 21-04
Запуск осуществляется из данного модуля.
CMD: python main.py

person.py - Описание сущностей
storage.py - Описание стратегий хранения
inp_out.py - Описание стратегий ввода вывода
group.py - контекст

"""

from inp_out import InputOutputWeb
from storage import InputOutPutFile
from flask import Flask, render_template, request
from group import Group
from person import Student, MainStudent

app = Flask(__name__)
group = Group(strategy_io=InputOutputWeb(), strategy_storage=InputOutPutFile())


@app.route("/", methods=['GET'])
def main():
    return render_template("main.html")


@app.route("/add-student", methods=['GET', 'POST'])
def add_student():
    if request.method == 'GET':
        return render_template('add_member.html')
    else:
        group.add(request=request, person=Student())
        return render_template('main.html', text='Участник добавлен!')


@app.route("/add-main", methods=['GET', 'POST'])
def add_main():
    if request.method == 'GET':
        return render_template('add_main.html')
    else:
        group.add(request=request, person=MainStudent())
        return render_template('main.html', text='Участник добавлен!')


@app.route("/clear-members", methods=['GET'])
def clear_members():
    group.delete_members()
    return render_template('main.html', text='Список участников пуст')


@app.route("/show", methods=['GET'])
def show():
    print(group.members)
    return render_template('show_members.html', data=group.members)


@app.route("/write-in-file", methods=['GET'])
def write_in_file():
    group.members_in_file()
    return render_template('main.html', text='Список загружен в файл!')


@app.route("/read-from-file", methods=['GET'])
def read_from_file():
    group.members_from_file()
    return render_template('main.html', text='Список загружен из файла!')


if __name__ == '__main__':
    app.run(app.run(debug=True))
