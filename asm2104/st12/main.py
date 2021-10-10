from group import Group
from consoleIO import ConsoleIO
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

group = Group()

def main():
	return render_template("main.html")

	menu = {
	1:('Добавить объект определенного типа',group.addNewPerson),
	2:('Удалить объект',group.deleteOneElement),
	3:('Вывести список',group.dumpAllObjects),
	4:('Сохранить в файл',group.dumpData),
	5:('Загрузить из файла',group.loadData),
	6:('Очистить список',group.clearList),
}

@app.route("/addNewPerson", methods=['GET'])
def addNewPerson():
    return render_template('addNewPerson.html')

@app.route("/deleteOneElement", methods=['POST'])
def deleteOneElement():
    group.deleteOneElement()

@app.route("/dumpAllObjects", methods=['POST'])
def dumpAllObjects():
    group.dumpAllObjects()

@app.route("/dumpData", methods=['POST'])
def dumpData():
    group.dumpData()

@app.route("/loadData", methods=['POST'])
def loadData():
    group.loadData()

@app.route("/clearList", methods=['POST'])
def clearList():
    group.clearList()

if __name__ == '__main__':
	main()
	app.run(app.run(debug=True))