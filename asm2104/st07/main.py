from CardFile import CardFile
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)
card = CardFile()

def main():
    return render_template("main.html")

@app.route("/add", methods=['GET'])
def add():
    return render_template('addElement.html')

@app.route("/clear", methods=['POST'])
def clear():
    card.clear()

@app.route("/print", methods=['POST'])
def print():
    card.print()

@app.route("/file_write", methods=['POST'])
def file_write():
    card.file_write()

@app.route("/file_read", methods=['POST'])
def file_read():
    card.file_read()

@app.route("/change", methods=['POST'])
def change():
    card.change()

@app.route("/changeOutput", methods=['POST'])
def changeOutput():
    card.changeOutput()


if __name__ == '__main__':
    app.run(app.run(debug=True))

