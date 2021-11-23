from student import Student


class Headman(Student):
    def __init__(self, id, name, surname, average_score, grant):
        super(Headman, self).__init__(id, name, surname, average_score)
        self.grant = grant

    def __str__(self):
        return super(Headman, self).__str__() + f' Стипендия: {self.grant}'
