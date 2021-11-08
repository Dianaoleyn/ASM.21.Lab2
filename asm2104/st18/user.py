
class user:
    def __init__(self, type='user'):
        self.id = -1
        self.name = ''
        self.age = int()
        self.type=type

    def __str__(self):
        text = f'Number: {self.id}\n' \
               f'Name: {self.name}\n' \
               f'Age: {self.age}\n'
        return text

    def output(self, strategy):
        return strategy(self).output()

    def input(self, strategy):
        strategy(self).input()