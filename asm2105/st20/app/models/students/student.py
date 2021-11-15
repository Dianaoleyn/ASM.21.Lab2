from asm2105.st20.app.models.cardItem import cardItem, ConsolePrintStrategy, ConsoleSetterStrategy, cardItemTypes

class student(cardItem):
    _group = str()
    _course = int()

    def __init__(self, print=ConsolePrintStrategy, setter=ConsoleSetterStrategy):
        cardItem.__init__(self, print, setter)
        self._type=cardItemTypes.student.value

    @property
    def group(self) -> str:
        return self._group

    @group.setter
    def group(self, group) -> None:
        self._group = group

    @property
    def course(self) -> int:
        return self._course

    @course.setter
    def course(self, course) -> None:
        self._course = course

    def __str__(self):
        text=super().__str__()
        text+=f'Группа: {self._group}\n' \
              f'Курс: {self._course}\n'
        return text


    def set_data(self, data):
        data=super().set_data(data)
        self._group=data['group']
        self._course=data['course']
        return data

    @staticmethod
    def get_attribs():
        attribs=cardItem.get_attribs()
        attribs['group']=['Группа', str]
        attribs['course']=['Курс', int]
        return attribs

    # def get_attribs(self):
    #     attr = super().get_attribs()
    #     attr['group'] = ['Группа', str]
    #     attr['course'] = ['Курс', int]
    #     return attr
    #
    # def set_data(self, attribs):
    #     super().set_data(attribs)
    #     self._group=attribs['group']
    #     self._course=attribs['course']
    #
    # def get_data(self):
    #     data=super().get_data()
    #     data['group']=self._group
    #     data['course']=self._course
    #     return data
