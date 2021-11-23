class Student:
    def __init__(self, id, name, surname, average_score):
        self.__create(id, name, surname, average_score)

    def __str__(self):
        return '{0} {1}. Средний балл: {2}. '.format(self.name, self.surname, self.average_score)

    def __create(self, id, name, surname, average_score):
        self.id = id
        self.name = name
        self.surname = surname
        self.average_score = average_score
