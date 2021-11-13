from group import Group
from schooler import Schooler
from teacher import Teacher
from flaskIO import FlaskIO
from fileIO import FileIO
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

group = Group()

@app.route('/')
def start():
    return render_template('mainMenu.html')

@app.route("/addNewSchooler", methods=['GET','POST'])
def addNewSchooler():
	if request.method=='GET':
		return render_template('addNewSchooler.html')
	else:
		group.list.append(Schooler(request.form['name'],request.form['surname'],request.form['rating'],request.form['characteristic']))
		return render_template('mainMenu.html')

@app.route("/addNewTeacher", methods=['GET','POST'])
def addNewTeacher():
	if request.method=='GET':
		return render_template('addNewTeacher.html')
	else:
		group.list.append(Teacher(request.form['name'],request.form['surname'],request.form['rating'],request.form['characteristic'],request.form['education'],request.form['subject']))
		return render_template('mainMenu.html')

@app.route("/dumpAllObjects", methods=['GET','POST'])
def dumpAllObjects():
	if request.method=='GET':
		group.strategy=FlaskIO
		return render_template('dumpAllObjects.html', data=group.dumpData())
	else:
		return render_template('mainMenu.html')

@app.route("/deleteOneElement",methods=['GET','POST'])
def deleteOneElement():
	if request.method=='GET':
		return render_template('deleteOneElement.html')
	else:
		group.deleteOneElement(request.form['num'])
		return render_template('mainMenu.html')

@app.route("/dumpData")
def dumpData():
	group.strategy=FileIO
	group.dumpData()
	return render_template('mainMenu.html')

@app.route("/loadData")
def loadData():
	group.loadData()
	return render_template('mainMenu.html')


@app.route("/clearList")
def clearList():
	group.clearList()
	return render_template('mainMenu.html')

if __name__ == '__main__':
	app.run()