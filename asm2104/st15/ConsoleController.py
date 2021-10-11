from administrator import Administrator
from salesman import Salesman
from shop import Shop
from Console import Console
from file import File

strategy = [
    {'label': 'Консоль', 'class': Console},
    {'label': 'Файл', 'class': File},
]

class ConsoleController:
    def getMenu(self, item):
        menu = [
            {'label': 'Добавить сотрудников', 'method': Shop.addEmployee},
            {'label': 'Очистить сотрудников', 'method': Shop.clearEmployees},
            {'label': 'Записать/вывести', 'method': Shop.showEmployees},
            {'label': 'Считать', 'method': Shop.getEmployees},
            {'label': 'Изменить стратегию', 'method': Shop.changeStrategy},
            {'label': 'Выйти'},
        ]
        while True:
            while True:
                for i in range(len(menu)):
                    print('{0}. {1}'.format(i, menu[i]['label']))
                try:
                    selected = int(input())
                    if selected == 5:
                        return
                    menu[selected]['method']()
                except:
                    print('Введите число от 0 до {}'.format(len(menu) - 1))


    def addElement(self):
        elementTypes = [
            {"type": "Продавец", "class": Salesman},
            {"type": "Администратор", "class": Administrator}
        ]
        for i in range(len(elementTypes)):
            print('{0}. {1}'.format(i, elementTypes[i]['text']))
        element = int(input())
        return elementTypes[element]['class']()


    def changeStrategy(self):
        print('Выберите вывод')
        for i in range(len(strategy)):
            print('{0}. {1}'.format(i, strategy[i]['text']))
        element = int(input())
        return strategy[element]['class']
