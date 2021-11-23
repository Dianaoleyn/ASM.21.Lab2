from zapis import zapis

class sluzh(zapis):
    def __init__(self):
        zapis.__init__(self)
        self.zarplata=int()
        self.stazh=int()

    def __str__(self):
        result=super().__str__()
        result+=f'Zarplata: {self.zarplata}\n' \
                f'Stazh: {self.stazh}\n'
        return result
