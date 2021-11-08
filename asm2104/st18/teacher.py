from employe import employe

class teacher(employe):
    def __init__(self, type='teacher'):
        employe.__init__(self, 'Teacher', type)
        self.subject=''

    def __str__(self):
        result=super().__str__()
        result+=f'Subject: {self.subject}\n'
        return result