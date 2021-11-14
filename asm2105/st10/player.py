class Player:
    def __init__(self, name=None, number=None, nationality=None):
        if name is None:
            self.name = input('Введите имя\n')
            self.number = input('Введите номер на футболке\n')
            self.nationality = input('Введите гражданство\n')
        else:
            self.name = name
            self.number = number
            self.nationality = nationality

    def __str__(self):
        return '{0}. Номер {1}. Гражданство: {2}. '.format(self.name, self.number, self.nationality)
