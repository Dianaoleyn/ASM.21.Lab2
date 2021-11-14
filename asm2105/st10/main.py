from flask import Flask, render_template, url_for, redirect
from fc import FC
from htmlIO import HtmlIO
from fileIO import FileIO

app = Flask(__name__)
FC = FC()


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route("/form", methods=['GET'])
def form_page():
    return render_template('form.html')


@app.route("/form", methods=['POST'])
def form_add():
    FC.write(HtmlIO)
    return go_to_main()


@app.route("/fc")
def list_page():
    return FC.read(HtmlIO)


@app.route("/file")
def file_page():
    return render_template('file.html')


@app.route("/clear")
def clear():
    FC.clearAll()
    return go_to_main()


@app.route("/load")
def file_load():
    FC.write(FileIO)
    return go_to_main()


@app.route("/save")
def file_save():
    FC.read(FileIO)
    return go_to_main()


def go_to_main():
    redirect(url_for('index'))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
