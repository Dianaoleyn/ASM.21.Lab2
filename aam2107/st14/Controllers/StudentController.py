from flask import Flask, g, request

from Services.IOServices.IOFormService import IOFormService
from Services.WebService import WebService

app = Flask(__name__)


def get_service():
    if 'WebService' not in g:
        g.web_service = WebService()
    return g.web_service

@app.route("/", methods=['GET'])
def index():
    return get_service().show_all()

@app.route("/showform/<int:id>")
def showform(id):
    return get_service().show_form(id)

@app.route("/showform/student", methods=['GET'])
def studentform():
    return get_service().show_student_form()

@app.route("/showform/main-student", methods=['GET'])
def mainstudentform():
    return get_service().show_main_student_form()

@app.route("/add", methods=['POST'])
def add():
    return get_service().add()

@app.route("/update", methods=['POST'])
def update():
    return get_service().update()

@app.route("/delete/<int:id>")
def delete(id):
    return get_service().delete(id)

@app.teardown_appcontext
def teardown_container(ctx):
    get_service().container.store_to_file()

if __name__ == "__main__":
    app.run(debug=True)
