if __name__ == '__main__':
    from kartoteka import MenuKartoteka
else:
    from .kartoteka import MenuKartoteka
from flask import Flask, request, redirect, url_for, g


app = Flask(__name__)


def GetCart():
    if 'cart' not in g:
        g.cart = MenuKartoteka()
        print('мда')
    return g.cart


@app.route("/")
def mainpage():
    return GetCart().print()


@app.route("/showform/<int:id>")
def showform(id):
    return GetCart().form_print(id)


@app.route("/add", methods=['POST'])
def add():
    case = request.form.get('capstud')
    return GetCart().add(case)


@app.route("/delete", methods=['GET'])
def delete():
    GetCart().clear()
    return redirect(url_for('mainpage'))


@app.route("/in_file", methods=['POST', 'GET'])
def in_file():
    GetCart().file_read()
    return redirect(url_for('mainpage'))


@app.route("/from_file", methods=['POST', 'GET'])
def from_file():
    GetCart().file_write()
    return redirect(url_for('mainpage'))


@app.teardown_appcontext
def print_in_file(ctx):
    return GetCart().file_read()


def main():
    app.run()


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
