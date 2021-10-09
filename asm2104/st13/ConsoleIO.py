from headman import Headman
from student import Student

elementTypes = [
    {'text': 'Добавить старосту', 'class': Headman},
    {'text': 'Добавить обычного студента', 'class': Student}
]


class ConsoleIO:
    @staticmethod
    def dump(arr):
        for el in arr:
            print(el)

    @staticmethod
    def load():
        arr = []
        print('Кого добавить')
        for i in range(len(elementTypes)):
            print('{0}. {1}'.format(i, elementTypes[i]['text']))
        element = int(input())
        number = int(input('Введите количество студентов\n'))
        for _ in range(number):
            arr.append(elementTypes[element]['class']())
        return arr
