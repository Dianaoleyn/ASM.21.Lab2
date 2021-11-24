from dinosaur import Dinosaur

class SuperDinosaur(Dinosaur):
    def __init__(self, strategy, type='Super'):
        super(SuperDinosaur, self).__init__(strategy, type)
        self.power = str()

    def __str__(self):
        return super(SuperDinosaur, self).__str__() + f'Power: {self.power}\n'
