from abc import ABC, abstractmethod
from student import Student
from typing import List

class StrategyIO(ABC):
    @abstractmethod
    def enter(self, person: Student):
        pass

    def printout(self, data: List):
        pass

class ConsoleIO(StrategyIO):
    def enter(self, person: Student):
        for key, val in person.__dict__.items():
            if key != 'is_VUC':
                person.__dict__[key] = input(f"{ key }: ")

    def printout(self, data: List):
        for person in data:
            for key, val in person.__dict__.items():
                print(f"{key} : {val}")


class WebIO(StrategyIO):
    def enter(self, person: Student, request=None):
        person.name = request.name
        person.surname = request.surname
        person.age = request.age
        person.rating = request.rating

    def printout(self, data: List):
        return 
