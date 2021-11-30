from GroupIndex import GroupIndex
from Member import MemberType

from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

index = GroupIndex()

type_dict = {'assistant': MemberType.ASSISTANT,
             'teacher': MemberType.TEACHER}

@app.route("/")
def root():
    return redirect(url_for('mainpage'))

@app.route("/group")
def mainpage():
    return index.show()

@app.route("/group/add_member_form")
def add_member_form():
    return render_template('add_member.html')

@app.route("/group/add_member", methods=['POST'])
def add_member():
    member_type = type_dict[request.form.get('member_type')]
    name = request.form.get('name')
    age = request.form.get('age')
    index.add(member_type, name, age)
    return redirect(url_for('mainpage'))

@app.route("/group/delete/<int:id>", methods=['GET'])
def delete_member(id):
    index.delete(id)
    return redirect(url_for('mainpage'))

@app.route("/group/clear", methods=['GET'])
def clear():
    index.clear()
    return redirect(url_for('mainpage'))

@app.route("/group/load", methods=['GET'])
def load():
    index.load()
    return redirect(url_for('mainpage'))

@app.route("/group/write", methods=['GET'])
def write():
    index.save()
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
