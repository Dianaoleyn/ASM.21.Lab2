from .Item import Item

class Student(Item):
    faculty=''
    group=''
    budget=bool()
    def __init__(self, strategy):
        Item.__init__(self, strategy)

    def __str__(self):
        text=super().__str__()
        text += 'Факультет: {} \n Группа: {} \n Бюджет(да/нет) {}\n'.format(self.faculty, self.group, self.budget)
        return text

    @staticmethod
    def get_attribs():
        attribs = Item.get_attribs()
        attribs['faculty'] = 'Факультет'
        attribs['group'] = 'Группа'
        attribs['budget'] = 'Бюджет'
        return attribs
    #
    # def set_attribs(self, in_dict):
    #     super().set_attribs(in_dict)
    #     self.faculty = in_dict['faculty']
    #     self.group = in_dict['group']
    #     self.budget = in_dict['budget']
