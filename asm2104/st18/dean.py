from employe import employe

class dean(employe):
    def __init__(self, type='dean'):
        employe.__init__(self, 'Dean', type)
        self.phone = ''

    def __str__(self):
        result = super().__str__()
        result += f'Phone: {self.phone}\n'
        return result