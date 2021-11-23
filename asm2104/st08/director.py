from employe import employe

class director(employe):
    def __init__(self):
        employe.__init__(self)
        self.phone=''
        self.cabinet=int()

    def __str__(self):
        result=super().__str__()
        result+=f'Phone: {self.phone}\n' \
                f'Cabinet: {self.cabinet}\n'
        return result