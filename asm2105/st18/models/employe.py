from .item import item

class employe(item):
    def __init__(self, interactive, type='employe'):
        item.__init__(self, interactive, type)
        self.roomNumber=int()

    def __str__(self):
        text=super().__str__()
        text+=f'Кабинет: {self.roomNumber}\n'
        return text