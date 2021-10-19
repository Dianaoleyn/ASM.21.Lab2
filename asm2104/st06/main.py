from flask import Flask, request, render_template, g

from asm2104.st06 import StorageIO
from asm2104.st06.ConsoleIO import ConsoleIO
from asm2104.st06.Html import Html
from asm2104.st06.StorageIO import Pickle, Shelve

if __name__ == '__main__':
    from Team import Team
else:
    from .Team import Team

app = Flask(__name__)

Team = Team()

# storage_strategy_list = [
#     {'text': 'Pickle', 'class': StorageIO.Pickle},
#     {'text': 'Shelve', 'class': StorageIO.Shelve},
# ]

strategy_list = [
    {'text': 'Pickle', 'class': Pickle},
    {'text': 'Shelve', 'class': Shelve},
    {'text': 'Console', 'class': ConsoleIO},
    {'text': 'HTML', 'class': Html}
]


def GetTeam():
    if 'Team' not in g:
        g.Team = Team
    return g.Team


@app.route("/")
def index():
    return GetTeam().index()


@app.route("/add_member", methods=['POST', 'GET'])
def add_member():
    if request.method == "POST":
        Team.add_member()
        return GetTeam().index()
    else:
        return render_template("add_member.html")


# @app.route("/edit_member", methods=['POST', 'GET'])
# def edit_member():
    # if Team.strategy == Html:
    #     if request.method == "POST":
    #         Team.edit_member()
    #         return GetTeam().index()
    #     else:
    #         return render_template("edit_member.html")
    # else:
    #     if request.method == "POST":
    #         return GetTeam().index()
    #     else:
    # Team.edit_member()


@app.route("/change_strategy", methods=['POST', 'GET'])
def change_strategy():
    if request.method == 'POST':
        for i in strategy_list:
            if i.get('text') == request.form.get('class'):
                Team.strategy = i.get('class')
                break
        return GetTeam().index()
    else:
        return Team.change_strategy()


# @app.route("/change_storage_strategy", methods=['POST', 'GET'])
# def change_storage_strategy():
#     if request.method == 'POST':
#         for i in strategy_list:
#             if i.get('text') == request.form.get('class'):
#                 Team.storage_strategy = i.get('class')
#                 break
#         return GetTeam().index()
#     else:
#         return Team.change_storage_strategy()


@app.route("/load", methods=['GET'])
def load():
    Team.load()
    return GetTeam().index()


@app.route("/dump", methods=['GET'])
def dump():
    dump = Team.dump()
    if (dump is None):
        return GetTeam().index()
    return Team.dump()


@app.route("/delete_members", methods=['GET'])
def delete_members():
    Team.delete_members()
    return GetTeam().index()


if __name__ == '__main__':
    app.run(debug=True)
