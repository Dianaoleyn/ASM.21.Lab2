from developer import Developer


class TeamLeader(Developer):
    def __init__(self, name=None, programLanguage=None, salary=None, annualBonus=None):
        if name is None:
            super(TeamLeader, self).__init__()
            self.annualBonus = input('Введите ежегодную премию\n')
        else:
            super(TeamLeader, self).__init__(name, programLanguage, salary)
            self.annualBonus = annualBonus

    def __str__(self):
        return super(TeamLeader, self).__str__() + f'Ежегодная премия: {self.annualBonus}'
