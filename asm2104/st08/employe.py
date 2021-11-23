from member import member

class employe(member):
    def __init__(self):
        member.__init__(self)
        self.salary=int()
        self.experience=int()

    def __str__(self):
        result=super().__str__()
        result+=f'Salary: {self.salary}\n' \
                f'Experience: {self.experience}\n'
        return result
