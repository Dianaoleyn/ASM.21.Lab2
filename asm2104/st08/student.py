from member import member

class student(member):
    def __init__(self):
        member.__init__(self)
        self.group=''
        self.course=int()

    def __str__(self):
        result=super().__str__()
        result+=f'Группа: {self.group}\n' \
                f'Курс: {self.course}\n'
        return result