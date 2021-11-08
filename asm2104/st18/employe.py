from user import user

class employe(user):
    def __init__(self, position='Employe', type='employe'):
        user.__init__(self, type)
        self.salary=int()
        self.experience=int()
        self.position=position

    def __str__(self):
        result=super().__str__()
        result+=f'Position: {self.position}' \
                f'Salary: {self.salary}\n' \
                f'Experience: {self.experience}\n'
        return result