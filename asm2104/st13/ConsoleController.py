from ConsoleIO import ConsoleIO
from HtmlController import HtmlController
from fileIO import FileIO
from headman import Headman
from student import Student

elementTypes = [
    {'text': 'Добавить старосту', 'class': Headman},
    {'text': 'Добавить обычного студента', 'class': Student}
]

classes = [
    {'text': 'Файл', 'class': FileIO},
    {'text': 'Консоль', 'class': ConsoleIO},
    {'text': 'HTML', 'class': HtmlController}
]

class ConsoleController:
    def getMenu(self, item):
        menu = [
            {'text': 'Добавить элемент', 'method': item.addElement},
            {'text': 'Очистить список', 'method': item.clearList},
            {'text': 'Отправить', 'method': item.dump},
            {'text': 'Получить', 'method': item.load},
        ]
        while True:
            for i in range(len(menu)):
                print('{0}. {1}'.format(i, menu[i]['text']))
            selected = int(input())
            menu[selected]['method']()


    def addElement(self):
        for i in range(len(elementTypes)):
            print('{0}. {1}'.format(i, elementTypes[i]['text']))
        element = int(input())
        return elementTypes[element]['class']()


    def changeStrategy(self):
        print('Выберите вывод')
        for i in range(len(classes)):
            print('{0}. {1}'.format(i, classes[i]['text']))
        element = int(input())
        return classes[element]['class']
