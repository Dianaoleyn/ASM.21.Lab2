from employe import employe

class teacher(employe):
    def __init__(self):
        employe.__init__(self)
        self.subject=''

    def __str__(self):
        result=super().__str__()
        result+=f'Subject: {self.subject}\n'
        return result

