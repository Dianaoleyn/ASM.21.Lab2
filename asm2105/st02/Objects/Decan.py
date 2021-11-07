from .Staff import Staff

class Decan(Staff):
    zav_faculty=''
    room_number=int()
    def __init__(self, strategy):
        Staff.__init__(self, strategy)

    def __str__(self):
        text = super().__str__()
        text += 'Факультет: {}\n Кабинет: {}\n'.format(self.zav_faculty, self.room_number)
        return text

    @staticmethod
    def get_attribs():
        attribs = Staff.get_attribs()
        attribs['zav_faculty'] = 'Факультет'
        attribs['official_number'] = 'Рабочий номер'
        attribs['room_number'] = 'Кабинет'
        return attribs