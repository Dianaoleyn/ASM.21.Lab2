from CardFile import CardFile
from Student import Student
from Monitor import Monitor
from StrategyIO import Web
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)
card = CardFile()

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/returnMain')
def returnMain():
    return render_template('main.html')

@app.route('/addStudent', methods=['GET', 'POST'])
def addStudent():
    if request.method=='GET':
        return render_template('addStudent.html')
    else:
        student = Student()
        Web.inputProperties(request.form,student)
        card.add(student)
        return render_template('addStudent.html')

@app.route('/addMonitor', methods=['GET', 'POST'])
def addMonitor():
    if request.method=='GET':
        return render_template('addMonitor.html')
    else:
        monitor = Monitor ()
        Web.inputProperties(request.form,monitor)
        card.add(monitor)
        return render_template('addMonitor.html')

@app.route("/updateStudent/<int:number>", methods=['GET','POST'])
def updateStudent(number):
	if request.method=='GET':
		return render_template('updateStudent.html',url=number)
	else:
		Web.inputProperties(request.form,card.card[number-1])
		return render_template('print.html', data=card.print())

@app.route("/updateMonitor/<int:number>", methods=['GET','POST'])
def updateMonitor(number):
	if request.method=='GET':
		return render_template('updateMonitor.html',url=number)
	else:
		Web.inputProperties(request.form,card.card[number-1])
		return render_template('print.html', data=card.print())

@app.route('/clear')
def clear():
    card.clear()
    return render_template('main.html')

@app.route('/print')
def print():
     return render_template('print.html', data=card.print())

@app.route('/file_write')
def file_write():
    card.file_write()
    return render_template('main.html')

@app.route('/file_read')
def file_read():
    card.file_read()
    return render_template('main.html')

@app.route("/delete/index/<int:number>")
def delete(number):
	card.delete(number)
	return render_template('print.html', data=card.print())

if __name__ == '__main__':
    app.run(app.run(debug=True))

