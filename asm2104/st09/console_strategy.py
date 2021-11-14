from developer import Developer
from team_leader import TeamLeader


menuList = [
    {'label': 'Добавить обычного разработчика', 'class': Developer},
    {'label': 'Добавить тимлида', 'class': TeamLeader}
]


class ConsoleStrategy:
    @staticmethod
    def dump(array):
        for item in array:
            print(item)

    @staticmethod
    def load():
        result = []
        counter = int(input('Сколько разработчиков добавляем?\n'))
        for i in range(counter):
            print('Выберите тип разработчика:')
            for j in range(len(menuList)):
                print('{0} - {1}'.format(j, menuList[j]['label']))

            result.append(menuList[int(input())]['class']())
        return result
