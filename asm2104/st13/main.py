if __name__ == '__main__':
    from AniList import AniList
    from Adaptation import Adaptation
    from Original import Original
else:
    from .AniList import AniList
    from .Adaptation import Adaptation
    from .Original import Original

from flask import Flask, request, render_template, url_for, redirect, url_for

app=Flask(__name__)
AniList=AniList()

@app.route('/')
def start():
    return render_template('mainMenu.html')

@app.route('/PrintAll')
def showAll():
    return render_template('printAll.html', data=AniList.print())

@app.route('/addAdaptation', methods=['GET', 'POST'])
def addAdaptation():
    if request.method=='GET':
        return render_template('addAdaptation.html')
    else:
        ent=Adaptation(request.form['name'],request.form['num'],request.form['genre'])
        AniList.add(ent)
        return render_template('addAdaptation.html')

@app.route('/addOriginal', methods=['GET', 'POST'])
def addOriginal():
    if request.method=='GET':
        return render_template('addOriginal.html')
    else:
        ent=Original(request.form['name'],request.form['genre'],request.form['num'])
        AniList.add(ent)
        return render_template('addOriginal.html')
    
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method=='GET':
        return render_template('delete.html')
    else:
        AniList.delete(int(request.form['ind'])-1)
        return render_template('delete.html')

@app.route('/loadData')
def loadData():
        AniList.file_read()
        return redirect('../')
    
@app.route('/dumpData')
def saveData():
        AniList.file_write()
        return redirect('../')
    
@app.route('/clear')
def clear():
        AniList.clear()
        return redirect('../')


if __name__ == '__main__':
    app.run()

