from asm2104.st06.Member import Member


class Player(Member):
    def __init__(self, name=None, surname=None, age=None, position=None):
        super(Player, self).__init__(name, surname, age)
        if position is None:
            self.position = input('Enter position\n')
        else:
            self.position = position

    def __str__(self):
        text = super().__str__()
        text += f'Position: {self.position}\n' \
                f'Member Type: Player'
        return text
