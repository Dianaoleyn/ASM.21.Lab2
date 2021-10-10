from musList import musList
from single import single
from album import album
from flask import Flask, request, render_template, url_for, redirect

app=Flask(__name__)
musList=musList()

@app.route('/')
def start():
    return render_template('mainMenu.html')

@app.route('/PrintAll')
def showAll():
    return render_template('printAll.html', data=musList.print())

@app.route('/addSingle', methods=['GET', 'POST'])
def addSingle():
    if request.method=='GET':
        return render_template('addSingle.html')
    else:
        ent=single(request.form['name'],request.form['year'],request.form['group'])
        musList.add(ent)
        return render_template('addSingle.html')

@app.route('/addAlbum', methods=['GET', 'POST'])
def addAlbum():
    if request.method=='GET':
        return render_template('addAlbum.html')
    else:
        ent=album(request.form['name'],request.form['year'],request.form['group'],request.form['num'])
        musList.add(ent)
        return render_template('addAlbum.html')
    
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method=='GET':
        return render_template('delete.html')
    else:
        musList.delete(int(request.form['ind'])-1)
        return render_template('delete.html')

@app.route('/loadData')
def loadData():
        musList.file_read()
        return redirect('../')
    
@app.route('/dumpData')
def saveData():
        musList.file_write()
        return redirect('../')
    
@app.route('/clear')
def clear():
    musList.clear()
    return redirect('../')


if __name__ == '__main__':
    app.run()

