from student import student

class groupLeader(student):
    def __init__(self, type='groupLeader'):
        student.__init__(self, type)
        self.email=''

    def __str__(self):
        result=super().__str__()
        result+=f'Email: {self.email}\n'
        return result