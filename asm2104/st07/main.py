from CardFile import CardFile
from Student import Student
from Monitor import Monitor
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
        student = Student(request.form['name'],request.form['surname'],request.form['age'])
        card.add(student)
        return render_template('addStudent.html')

@app.route('/addMonitor', methods=['GET', 'POST'])
def addMonitor():
    if request.method=='GET':
        return render_template('addMonitor.html')
    else:
        monitor = Monitor (request.form['name'],request.form['surname'],request.form['age'],request.form['increasedScholarship'])
        card.add(monitor)
        return render_template('addMonitor.html')

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

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method=='GET':
        return render_template('delete.html')
    else:
        card.delete(int(request.form['index']))
        return render_template('delete.html')

if __name__ == '__main__':
    app.run(app.run(debug=True))

