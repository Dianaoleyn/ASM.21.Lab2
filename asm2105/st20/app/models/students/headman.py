from ..students.student import student, ConsolePrintStrategy, ConsoleSetterStrategy
from ...strategys.checkPhoneNumStrategys import CheckMobilePhoneNumWithPlusStrategy


class headman(student):
    _phone = str()
    def __init__(self, check_phone_strategy=CheckMobilePhoneNumWithPlusStrategy(), print=ConsolePrintStrategy, setter=ConsoleSetterStrategy):
        student.__init__(self, print, setter)
        self.check_phone_strategy=check_phone_strategy

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, phone) -> None:
        if self.check_phone_strategy.check(phone):
            self._phone = phone
        else:
            raise Exception('Телефон не соответствует заданному формату')

    def __str__(self):
        text = super().__str__()
        text += f'Телефон: {self.phone}\n'
        return text

    def set_data(self, data):
        data=super().set_data(data)
        self.phone=data['phone']
        return data

    @staticmethod
    def get_attribs():
        attribs=student.get_attribs()
        attribs['phone']=['Телефон', str]
        return attribs
