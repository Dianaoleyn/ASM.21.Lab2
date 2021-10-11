from student import Student


class Headman(Student):
    def __init__(self, name=None, surname=None, score=None, additionalScholarship=None):
        super(Headman, self).__init__(name, surname, score)
        if additionalScholarship is None:
            self.additionalScholarship = input('Введите дополнительную стипендию\n')
        else:
            self.additionalScholarship = additionalScholarship

    def __str__(self):
        return super(Headman, self).__str__() + 'Дополнительная стипендия: {}'.format(self.additionalScholarship)

