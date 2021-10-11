from .Player import Player


class Captain(Player):
    def __init__(self, name='', surname='', age='', exp=''):
        super().__init__(name, surname, age)
        self.experience = exp

    def __str__(self):
        return super().__str__() + f' Опыт { self.experience }'

