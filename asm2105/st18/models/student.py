
from .item import item

class student(item):
    def __init__(self, interactive, type='student'):
        item.__init__(self, interactive, type)
        self.course=int()
        self.group=''

    def __str__(self):
        text=super().__str__()
        text+=f'Курс: {self.course}\n' \
              f'Группа: {self.group}\n'
        return text
