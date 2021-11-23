from sluzh import sluzh

class teacher(sluzh):
    def __init__(self):
        sluzh.__init__(self)
        self.predmet=''

    def __str__(self):
        result=super().__str__()
        result+=f'Predmet: {self.predmet}\n'
        return result