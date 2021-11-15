from asm2105.st20.app.models.cardItem import cardItem, ConsoleSetterStrategy, ConsolePrintStrategy, cardItemTypes

class worker(cardItem):
    _salary = int()
    def __init__(self, print=ConsolePrintStrategy, setter=ConsoleSetterStrategy):
        cardItem.__init__(self, print, setter)
        self._type=cardItemTypes.worker.value


    @property
    def salary(self) -> int:
        return self._salary

    @salary.setter
    def salary(self, salary) -> None:
        self._salary = salary


    def __str__(self):
        text=super().__str__()
        text+=f'Зарплата: {self._salary}\n'
        return text

    def set_data(self, data):
        data=super().set_data(data)
        self.salary=data['salary']
        return data

    @staticmethod
    def get_attribs():
        attribs=cardItem.get_attribs()
        attribs['salary']=['Зарплата', int]
        return attribs


