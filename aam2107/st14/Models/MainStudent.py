from dataclasses import dataclass
from aam2107.st14.Models.Student import Student


@dataclass
class MainStudent(Student):
    email: str = ''

    def __str__(self) -> str:
        """Получить объект класса студента в строковом виде"""
        return f'\nФИО: {self.last_name} {self.first_name} {self.middle_name};\n' \
               f'Возраст: {self.age};\n' \
               f'Средний балл: {self.average_score}\n' \
               f'Почта группы: {self.email}'