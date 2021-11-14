from player import Player


class Captain(Player):
    def __init__(self, name=None, number=None, nationality=None, age=None):
        if name is None:
            super(Captain, self).__init__()
            self.age = input('Введите возраст\n')
        else:
            super(Captain, self).__init__(name, number, nationality)
            self.age = age

    def __str__(self):
        return super(Captain, self).__str__() + f'Возраст: {self.age}'
