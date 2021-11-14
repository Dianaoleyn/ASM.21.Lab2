from flask import Flask, request, redirect, url_for
from .Team import Team

app = Flask(__name__)

TeamList = Team()


@app.route("/")
def start():
    return TeamList.print()


@app.route("/showform/<int:id>")
def showform(id):
    return TeamList.form_print(id)


@app.route("/add", methods=['POST'])
def add():
    case = request.form.get('capstud')
    return TeamList.add(case)


@app.route("/delete", methods=['GET'])
def delete():
    TeamList.clear()
    return redirect(url_for('start'))


@app.route("/write_file", methods=['POST', 'GET'])
def in_file():
    TeamList.write_file()
    return redirect(url_for('start'))


@app.route("/read_file", methods=['POST', 'GET'])
def from_file():
    TeamList.read_file()
    return redirect(url_for('start'))


def main():
    app.run()


if __name__ == "__main__":
    main()