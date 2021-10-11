class Student:
    def __init__(self, name=None, surname=None, score=None):
        if name is None:
            self.name = input('Введите имя\n')
            self.surname = input('Введите фамилию\n')
            self.averageRating = input('Введите средний балл\n')
        else:
            self.name = name
            self.surname = surname
            self.averageRating = score

    def __str__(self):
        return '{0} {1}. Средний балл: {2}. '.format(self.surname, self.name, self.averageRating)
