from flask import Flask, render_template, request
from student import Student
from Student_VUC import Student_VUC
from group import Group
from StrategyIO import WebIO
from StrategyFileIO import FileIO

app = Flask(__name__)
group = Group(strategyFile=FileIO(), strategyIO=WebIO())

if __name__ == '__main__':
    from group import group
else:
    from .group import group


@app.route("/", methods=['GET'])
def main():
    return render_template("main.html")


@app.route("/add-student", methods=['GET', 'POST'])
def add_student():
    if request.method == 'GET':
        return render_template('addStudent.html')
    else:
        group.add(request=request, person=Student())
        return render_template('main.html', text='Участник добавлен!')


@app.route("/delete-all", methods=['GET'])
def clear_members():
    group.clear_kartoteka()
    return render_template('main.html', text='Картотека почищена')


@app.route("/show", methods=['GET'])
def show():
    print(group.cartoteka)
    return render_template('printKartoteka.html', data=group.members)


@app.route("/save-to-file", methods=['GET'])
def write_in_file():
    group.cartoteka_in_file()
    return render_template('main.html', text='Сохранено в файл')


@app.route("/read-from-file", methods=['GET'])
def read_from_file():
    group.cartoteka_from_file()
    return render_template('main.html', text='Загружено из файла')


if __name__ == "__main__":
    app.run(debug=True)
