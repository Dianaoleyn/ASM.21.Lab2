from abc import ABCMeta

from asm2105.st04.inputstrategy import InputStrategy


class Member(metaclass=ABCMeta):
    id: int = 0
    name: str = ''
    second_name: str = ''
    stipend: int = 0
    input_strategy = InputStrategy.default

    def getData(self, id):
        self.id = id
        self.name = self.input_strategy('name')
        self.second_name = self.input_strategy('secondName')
