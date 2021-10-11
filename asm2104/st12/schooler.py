class Schooler:
    def __init__(self):
        self.name = input('Введите имя\n')
        self.surname = input('Введите фамилию\n')
        self.rating = input('Введите рейтинг\n')
        self.characteristic = input('Введите характеристику\n')


    def __str__(self):
        return "Имя: {}, Фамилия: {}, Рейтинг: {}, Характеристика: {}".format(self.name, self.surname, self.rating,self.characteristic)