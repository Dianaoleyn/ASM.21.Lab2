from Company import Company
from File import File
from Console import Console
from Html import Html
from flask import Flask, render_template, request

app = Flask(__name__)

company = Company()

strategy_type = [
    {'title': 'File', 'class': File},
    {'title': 'Console', 'class': Console},
    {'title': 'HTML5', 'class': Html}
]


@app.route("/")
def get_menu():
    return company.get_menu()


@app.route("/add_employee", methods=['POST', 'GET'])
def add_employee():
    if company.strategy == Html:
        if request.method == 'POST':
            company.add_employee()
            return company.get_menu()
        else:
            return render_template('add_employee.html')
    else:
        return render_template('warning.html', active_strategy=company.strategy.__name__)


@app.route("/edit_employee/<int:id>", methods=['POST', 'GET'])
def edit_employee(id):
    if company.strategy == Html:
        if request.method == 'POST':
            company.edit_employee(id)
            return company.get_menu()
        else:
            return render_template('edit_employee.html')
    else:
        return render_template('warning.html', active_strategy=company.strategy.__name__)


@app.route("/delete_employee/<int:id>")
def delete_employee(id):
    if company.strategy == Html:
        company.delete_employee(id)
        return company.get_menu()
    else:
        return render_template('warning.html', active_strategy=company.strategy.__name__)


@app.route("/clear_employee_list", methods=['GET'])
def clear_employee_list():
    if company.strategy == Html:
        company.clear_employee_list()
        return company.get_menu()
    else:
        return render_template('warning.html', active_strategy=company.strategy.__name__)


@app.route("/input_data", methods=['POST', 'GET'])
def input_data():
    if company.strategy == Html:
        if request.method == 'POST':
            company.input_employee_list()
            return company.get_menu()
        else:
            return render_template('io_select.html', classes=strategy_type)
    return render_template('warning.html', active_strategy=company.strategy.__name__)


@app.route("/output_data", methods=['POST', 'GET'])
def output_data():
    if company.strategy == Html:
        if request.method == 'POST':
            company.output_employee_list()
            return company.get_menu()
        else:
            return render_template('io_select.html', classes=strategy_type)
    return render_template('warning.html', active_strategy=company.strategy.__name__)


@app.route("/change_strategy", methods=['POST', 'GET'])
def change_strategy():
    if company.strategy == Html:
        if request.method == 'POST':
            company.change_strategy()
            return company.get_menu()
        else:
            return render_template('change_strategy.html', classes=strategy_type[1:])
    return render_template('warning.html', active_strategy=company.strategy.__name__)


if __name__ == '__main__':
    app.run(app.run(debug=True))
