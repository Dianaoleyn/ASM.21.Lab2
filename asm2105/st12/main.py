from flask import Flask, request, redirect, url_for
if __name__ == '__main__':
    from kartoteka import MenuCartoteka
else:
    from .kartoteka import MenuCartoteka

app = Flask(__name__)

cart = MenuCartoteka()


@app.route("/")
def mainpage():
    return cart.print()


@app.route("/showform/<int:id>")
def showform(id):
    return cart.form_print(id)


@app.route("/add", methods=['POST'])
def add():
    case = request.form.get('capstud')
    return cart.add(case)


@app.route("/delete", methods=['GET'])
def delete():
    cart.clear()
    return redirect(url_for('mainpage'))


@app.route("/in_file", methods=['POST', 'GET'])
def in_file():
    cart.file_read()
    return redirect(url_for('mainpage'))


@app.route("/from_file", methods=['POST', 'GET'])
def from_file():
    cart.file_write()
    return redirect(url_for('mainpage'))


def main():
    app.run()


if __name__ == "__main__":
    main()
    """
    pipenv shell
    set FLASK_APP=main.py
    flask run
    """
