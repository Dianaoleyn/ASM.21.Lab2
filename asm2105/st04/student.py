from abc import ABC
from dataclasses import dataclass

from asm2105.st04.member import Member


@dataclass()
class Student(Member, ABC):
    type: str = 'Студент'
    stipend: int = 2000
    
    def getData(self, id):
        super(Student, self).getData(id)
