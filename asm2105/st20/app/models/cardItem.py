from asm2105.st20.app.strategys.printStrategys import ConsolePrintStrategy
from asm2105.st20.app.strategys.setterStrategy import ConsoleSetterStrategy

class cardItem:
    _id = -1
    _name = str()
    _age = int()
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

    def __str__(self):
        text = f'Номер: {self._id}\n' \
               f'Имя: {self._name}\n' \
               f'Возраст: {self._age}\n'
        return text

    def print(self):
        self._printer.print()

    def set_data(self, data):
        data=self._setter.to_dict(data)
        # self._id=data['id']
        self._name=data['name']
        self._age=data['age']
        return data

    @staticmethod
    def get_attribs():
        attribs={
            'name':['Имя', str],
            'age':['Возраст', int]
        }
        return attribs

    # def set_data(self, attribs):
    #     self._id=attribs['id']
    #     self._age = attribs['age']
    #     self._name = attribs['name']
    #
    # def get_data(self):
    #     data={
    #         'id':self._id,
    #         'name':self._name,
    #         'age':self._age
    #     }
    #     return data