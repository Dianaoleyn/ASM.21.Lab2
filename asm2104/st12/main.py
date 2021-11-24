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

@app.route("/updateSchooler/<int:number>", methods=['GET','POST'])
def updateNewSchooler(number):
	if request.method=='GET':
		return render_template('updateSchooler.html',url=number)
	else:
		group.ChangeEl(number,request.form)
		return render_template('mainMenu.html')

@app.route("/updateTeacher/<int:number>", methods=['GET','POST'])
def updateTeacher(number):
	if request.method=='GET':
		return render_template('updateTeacher.html',url=number)
	else:
		group.ChangeEl(number,request.form)
		return render_template('mainMenu.html')

@app.route("/addNewSchooler", methods=['GET','POST'])
def addNewSchooler():
	if request.method=='GET':
		return render_template('addNewSchooler.html')
	else:
		group.add(Schooler(),request.form)
		return render_template('mainMenu.html')

@app.route("/addNewTeacher", methods=['GET','POST'])
def addNewTeacher():
	if request.method=='GET':
		return render_template('addNewTeacher.html')
	else:
		group.add(Teacher(),request.form)
		return render_template('mainMenu.html')

@app.route("/dumpAllObjects", methods=['GET','POST'])
def dumpAllObjects():
	if request.method=='GET':
		group.strategy=FlaskIO
		return render_template('dumpAllObjects.html', data=group.dumpData())
	else:
		return render_template('mainMenu.html')

@app.route("/delete/index/<int:number>")
def delete(number):
	group.deleteOneElement(number)
	group.strategy=FlaskIO
	return render_template('dumpAllObjects.html', data=group.dumpData())

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