from student import student

class starosta(student):
    def __init__(self):
        student.__init__(self)
        self.email=''

    def __str__(self):
        result=super().__str__()
        result+=f'Email: {self.email}\n'
        return result