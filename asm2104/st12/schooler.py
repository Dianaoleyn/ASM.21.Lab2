class Schooler:
    def __init__(self,name,surname,rating,characteristic):
        self.name = name
        self.surname = surname
        self.rating = rating
        self.characteristic = characteristic


    def __str__(self):
        return "Имя: {}, Фамилия: {}, Рейтинг: {}, Характеристика: {}".format(self.name, self.surname, self.rating,self.characteristic)