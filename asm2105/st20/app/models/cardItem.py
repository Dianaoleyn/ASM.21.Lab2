from ..strategys.printStrategys import ConsolePrintStrategy
from ..strategys.setterStrategy import ConsoleSetterStrategy
import enum

class cardItemTypes(enum.Enum):
    empty='Пустая запись'
    worker='Служащий'
    teacher='Преподаватель'
    student='Студент'
    headman='Староста'

class cardItem:
    _id = -1
    _name = str()
    _age = int()
    _type = cardItemTypes.empty.value
    def __init__(self, print=ConsolePrintStrategy, setter=ConsoleSetterStrategy):
        self._printer=print(self)
        self._setter=setter()

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id) -> None:
        self._id = int(id)

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age) -> None:
        self._age = int(age)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        self._name = name

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, type) -> None:
        self._type = type


    def __str__(self):
        text = f'Номер: {self._id}\n' \
               f'Тип: {self._type}\n' \
               f'Имя: {self._name}\n' \
               f'Возраст: {self._age}\n'
        return text

    def print(self):
        return self._printer.print()

    def set_data(self, data):
        data=self._setter.to_dict(data)
        # self._id=data['id']
        self._name=data['name']
        self._age=data['age']
        return data

    def set(self):
        self._setter.set(self)


    @staticmethod
    def get_attribs():
        attribs={
            'name':['Имя', str],
            'age':['Возраст', int],
            'type':['Тип записи', str]
        }
        return attribs


