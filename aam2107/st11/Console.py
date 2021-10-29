from admin import Admin
from pharman import Pharman


class Console:
    def getEmployees(self):
        types = [
            {"type": "Фармацевт", "class": Pharman},
            {"type": "Администратор", "class": Admin}
        ]
        for i in range(len(types)):
            print('{0}. {1}'.format(i, types[i]['type']))
        selectedClass = ''
        try:
            selected = int(input())
            selectedClass = types[selected]['class']
        except:
            print('Введите число от 0 до {}'.format(len(types) - 1))

        try:
            count = int(input('Введите количество\n'))
            returningList = []
            for _ in range(count):
                returningList.append(selectedClass.newPharman())
            return returningList
        except:
            print('Введите корректные данные')

    def showEmployees(self, employees):
        for emp in employees:
            print(emp)
