from group import Group
from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)
group = Group()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET'])
def add_form():
    return group.add_element_form()


@app.route('/form/<int:id>', methods=['GET'])
def edit_form(id):
    return group.edit_element_form(id)


@app.route('/form', methods=['Post'])
def add():
    group.add_element()
    return return_home()


@app.route('/form/<int:id>', methods=['Post'])
def edit(id):
    group.edit_element(id)
    return return_home()


@app.route('/group')
def group_list():
    return group.show_elements()


@app.route('/clear')
def clear():
    group.delete_all()
    return return_home()


@app.route('/delete/<int:id>')
def delete_element(id):
    group.delete_element(id)
    return return_home()


@app.route('/save')
def save():
    group.save_all_elements()
    return return_home()


def return_home():
    redirect(url_for('index'))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
