from student import Student
from headman import Headman


class ConsoleIO:
    @staticmethod
    def output(array):
        for item in array:
            print(item)

    @staticmethod
    def input():
        menu = [
            {'label': 'Добавить студента', 'class': Student},
            {'label': 'Добавить старосту', 'class': Headman}
        ]
        for i in range(len(menu)):
            print('{0} - {1}'.format(i, menu[i]['label']))

        return menu[int(input())]['class']()
