from asm2105.st20.app.models.workers.worker import worker, ConsoleSetterStrategy, ConsolePrintStrategy, cardItemTypes


class teacher(worker):
    _subject = str()
    def __init__(self, print=ConsolePrintStrategy, setter=ConsoleSetterStrategy):
        worker.__init__(self, print, setter)
        self._type=cardItemTypes.teacher.value


    @property
    def subject(self) -> str:
        return self._subject

    @subject.setter
    def subject(self, subject) -> None:
        self._subject = subject

    def __str__(self):
        text = super().__str__()
        text += f'Предмет: {self.subject}\n'
        return text

    def set_data(self, data):
        data = super().set_data(data)
        self.subject = data['subject']
        return data

    @staticmethod
    def get_attribs():
        attribs = worker.get_attribs()
        attribs['subject'] = ['Предмет', str]
        return attribs