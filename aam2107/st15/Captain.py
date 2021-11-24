from Student import Student



class Captain(Student):
    def __init__(self, name='', surname='', age='', grants=''):
        super().__init__(name, surname, age)
        self.__grants = grants

    def __str__(self):
        return super().__str__() + f', Надбавка { self.__grants }'

