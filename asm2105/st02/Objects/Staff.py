from .Item import Item

class Staff(Item):
    post=''
    experience=''
    def __init__(self, strategy):
        Item.__init__(self, strategy)

    def __str__(self):
        text = super().__str__()
        text += 'Занимаемая должность: {} \n Стаж работы: {} \n'.format(self.post, self.experience)
        return text


    @staticmethod
    def get_attribs():
        attribs = Item.get_attribs()
        attribs['post'] = 'Занимаемая должность'
        attribs['experience'] = 'Cтаж работы'
        return attribs