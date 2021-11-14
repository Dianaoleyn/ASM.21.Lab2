from flask import Flask, request, render_template, g, redirect

from ConsoleIO import ConsoleIO
from Html import Html
from StorageIO import Pickle

if __name__ == '__main__':
    from Team import Team
else:
    from .Team import Team

app = Flask(__name__)

Team = Team()

strategy_list = [
    {'text': 'Pickle', 'class': Pickle},
    {'text': 'Console', 'class': ConsoleIO},
    {'text': 'HTML', 'class': Html}
]


def get_team():
    if 'Team' not in g:
        g.Team = Team
    return g.Team


@app.route("/")
def index():
    return get_team().index()


@app.route("/add_member", methods=['POST', 'GET'])
def add_member():
    if get_team().strategy == ConsoleIO:
        get_team().add_member()
        return get_team().index()
    else:
        if request.method == "POST":
            get_team().add_member()
            return get_team().index()
        else:
            return render_template("add_member.html")


@app.route("/edit_member/<int:id>", methods=['POST', 'GET'])
def edit_member(id):
    if request.method == "POST":
        get_team().edit_member(id)
        return get_team().index()
    else:
        return render_template("edit_member.html")


@app.route("/change_strategy", methods=['POST', 'GET'])
def change_strategy():
    if request.method == 'POST':
        for i in strategy_list:
            if i.get('text') == request.form.get('class'):
                get_team().strategy = i.get('class')
                break
        return get_team().index()
    else:
        return get_team().change_strategy()


@app.route("/load", methods=['GET'])
def load():
    if get_team().strategy == Html:
        return redirect("/add_member")
    elif get_team().strategy == ConsoleIO:
        get_team().add_member()
        return get_team().index()
    else:
        get_team().load()
        return get_team().index()


@app.route("/dump", methods=['GET'])
def dump():
    dump = get_team().dump()
    if (dump is None):
        return get_team().index()
    return get_team().dump()


@app.route("/delete_members", methods=['GET'])
def delete_members():
    get_team().delete_all()
    return get_team().index()


@app.route("/delete_member/<int:id>")
def delete_member(id):
    get_team().delete_member(id)
    return get_team().index()


if __name__ == '__main__':
    app.run(app.run(debug=True))
