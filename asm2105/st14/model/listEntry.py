from enum import IntEnum

class Types(IntEnum):
    listEntry=0
    student=1
    starosta=2
    worker=3
    teacher=4
    director=5


class listEntry:

    def __init__(self, strategy):
        self.id = -1
        self.name = ''
        self.age = ''
        self.strategy=strategy(self)
        self.type=Types.listEntry

    def __str__(self):
        text=f'Номер: {self.id}\n' \
             f'Имя: {self.name}\n' \
             f'Возраст: {self.age}\n'
        return text

    def Out(self):
        return self.strategy.Out()

    def In(self):
        self.strategy.In()

