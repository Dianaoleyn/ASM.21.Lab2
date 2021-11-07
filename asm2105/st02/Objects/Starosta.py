from .Student import Student

class Starosta(Student):
    group_mail=''
    phone_number=''
    def __init__(self, strategy):
        Student.__init__(self, strategy)

    def __str__(self):
        text = super().__str__()
        text += 'Почта группы: {} \n Номер старосты: {} \n'.format(self.group_mail, self.phone_number)
        return text

    @staticmethod
    def get_attribs():
        attribs = Student.get_attribs()
        attribs['group_mail'] = 'Почта группы'
        attribs['phone_number'] = 'Номер старосты'
        return attribs
