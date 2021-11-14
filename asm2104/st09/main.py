from flask import Flask
from company import Company
from html_strategy import HtmlStrategy
from file_strategy import FileStrategy

app = Flask(__name__)
company = Company([])


@app.route('/')
def index():
    return HtmlStrategy.home()


@app.route("/add", methods=['GET'])
def addGet():
    return HtmlStrategy.add()


@app.route("/add", methods=['POST'])
def addPost():
    company.addElements(HtmlStrategy)
    return HtmlStrategy.message('Элемент был добавлен')


@app.route("/list")
def listGet():
    return company.getElements(HtmlStrategy)


@app.route("/clear")
def listClear():
    company.clearAllElements()
    return HtmlStrategy.message('Список был очищен')


@app.route("/load")
def load():
    company.addElements(FileStrategy)
    return HtmlStrategy.message('Загрузил!')


@app.route("/save")
def save():
    company.getElements(FileStrategy)
    return HtmlStrategy.message('Сохранил!')


if __name__ == "__main__":
    app.run(debug=True)
