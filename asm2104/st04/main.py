from group import Group
from consoleIO import ConsoleIO
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)
group=Group()

def main():
	return render_template("main.html")

@app.route("/addElement", methods=['GET'])
def addElement():
    return render_template('addElement.html')

@app.route("/clearList", methods=['POST'])
def clearList():
    group.clearList()

@app.route("/outputList", methods=['POST'])
def outputList():
    group.outputConsole()

@app.route("/outputFile", methods=['POST'])
def outputFile():
    group.outputFile()

@app.route("/inputFile", methods=['POST'])
def inputFile():
    group.inputFile()

@app.route("/deleteObject", methods=['POST'])
def deleteObject():
    group.deleteObject()

@app.route("/editObject", methods=['POST'])
def editObject():
    group.editObject()


if __name__ == '__main__':
	app.run(app.run(debug=True))