from group import Group
from student import Student 
from head import Head
from webIO import WebIO
from fileIO import FileIO
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)
group=Group()

@app.route('/')
def start():
    return render_template('main.html')

@app.route('/returnMain')
def returnMain():
    return render_template('main.html')

@app.route("/addHead",methods=['GET','POST'])
def addHead():
    if request.method=='GET':
        return render_template('addHead.html')
    else:
        if(request.form.__contains__('check')):
            group.addElement(Head,FileIO(),request.form)
        else:
            group.addElement(Head,WebIO(),request.form)
        return render_template('addHead.html')

@app.route("/addStudent",methods=['GET','POST'])
def addStudent():
    if request.method=='GET':
        return render_template('addStudent.html')
    else:
        if(request.form.__contains__('check')):
            group.addElement(Student,FileIO(),request.form)
        else:
            group.addElement(Student,WebIO(),request.form)
        return render_template('addStudent.html')

@app.route("/deleteObj/<int:id>")
def deleteObj(id):
    group.deleteObject(id)
    WebData=group.outputWeb()
    return render_template('outputList.html',data=WebData)

@app.route("/clearList")
def clearList():
    group.clearList()
    return render_template('main.html')

@app.route("/addElement")
def addElement():
    return render_template('addElement.html')

@app.route("/outputList", methods=['GET'])
def outputList():
    WebData=group.outputWeb()
    return render_template('outputList.html', data=WebData)

@app.route("/outputFile")
def outputFile():
    group.outputFile()
    return render_template('main.html')

@app.route("/inputFile")
def inputFile():
    group.inputFile()
    return render_template('main.html')

# @app.route("/deleteObject",methods=['GET','POST'])
# def deleteObject():
#     if request.method=='GET':
#         return render_template('deleteObject.html')
#     else:
#         group.deleteObject(request.form['index'])
#         return render_template('main.html')

if __name__ == '__main__':
	app.run()