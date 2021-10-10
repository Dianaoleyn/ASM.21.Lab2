from flask import Flask, request, redirect, url_for
from .kartoteka import MenuKartoteka

app = Flask(__name__)

archive = MenuKartoteka()


@app.route("/")
def start():
    return archive.print()


@app.route("/showform/<int:id>")
def showform(id):
    return archive.form_print(id)


@app.route("/add", methods=['POST'])
def add():
    case = request.form.get('capstud')
    return archive.add(case)


@app.route("/delete", methods=['GET'])
def delete():
    archive.clear()
    return redirect(url_for('start'))


@app.route("/in_file", methods=['POST', 'GET'])
def in_file():
    archive.file_write()
    return redirect(url_for('start'))


@app.route("/from_file", methods=['POST', 'GET'])
def from_file():
    archive.file_read()
    return redirect(url_for('start'))


def main():
    app.run()


if __name__ == "__main__":
    main()
