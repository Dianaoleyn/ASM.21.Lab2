class Schooler:
    # def __init__(self,name,surname,rating,characteristic):
    #     self.name = name
    #     self.surname = surname
    #     self.rating = rating
    #     self.characteristic = characteristic


    def __str__(self):
        return "Имя: {}, Фамилия: {}, Рейтинг: {}, Характеристика: {}".format(self.name, self.surname, self.rating,self.characteristic)

    def strWeb(self,index):
        href='/delete/index/'+index.__str__()
        hrefUpdate='/updateSchooler/'+index.__str__()
        return "Имя: {}, Фамилия: {}, Рейтинг: {}, Характеристика: {}".format(self.name, self.surname, self.rating,self.characteristic)+'<a href="'+href+'">Удалить</a><br>'+'<a href="'+hrefUpdate+'">Изменить</a><br>'