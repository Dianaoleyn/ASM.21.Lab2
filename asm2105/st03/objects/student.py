from .item import item

class student(item):

    def __init__(self, strategy, type='student'):
        item.__init__(self, strategy, type)
        self.group=''

    def __str__(self):
        text=super().__str__()
        text+=f'Группа: {self.group}\n'
        return text


