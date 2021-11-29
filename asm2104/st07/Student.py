class Student:
    def __init__(self, name='', surname='', age=''):
        self.name = name
        self.surname = surname
        self.age = age

    def input(self):
        self.name = input("Имя: ")
        self.surname = input("Фамилия: ")
        self.age = int(input("Возраст: "))

    def strShort(self):
        return f'Фамилия: { self.surname }, Возраст: { self.age },'

    def strFull(self):
        return "Имя: {}, Фамилия: {}, Возраст: {}".format(
            self.name, self.surname, self.age
        )
    def strWeb(self,index):
        urlDelete='/delete/index/'+index.__str__()
        urlUpdate='/updateStudent/'+index.__str__()
        return self.name+"<br />"+self.surname+"<br />"+self.age+"<br />"+'<a href="'+urlDelete+'">Удалить</a><br>'+'<a href="'+urlUpdate+'">Изменить</a><br>'"<br />"
