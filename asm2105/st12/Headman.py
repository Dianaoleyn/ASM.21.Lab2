from Student import Student



class Headman(Student):
    def __init__(self, name='', surname='', age='', premium=''):
        super().__init__(name, surname, age)
        self.__premium = premium

    def __str__(self):
        return super().__str__() + f', Надбавка { self.__premium }'

