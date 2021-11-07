class Item:
    number=-1
    name=''
    age=int()
    russian_sitizenship=''
    gender=''
    def __init__(self, strategy):
        self.strategy=strategy(self)

    def __str__(self):
        text = 'Номер: {}\n Имя: {}\n Возраст: {}\n Пол: {}\n  Гражданство РФ: {}\n '.format(self.number, self.name, self.age, self.gender, self.russian_sitizenship)
        return text

    def print(self):
        return self.strategy.print()

    def set(self):
        self.strategy.set()

    @staticmethod
    def get_attribs():
        output_dict = {}
        output_dict['name'] = 'Имя'
        output_dict['age'] = 'Возраст'
        output_dict['gender'] = 'Пол (М/Ж)'
        output_dict['russian_sitizenship'] = 'Гражданство РФ (1/0)'
        return output_dict
    #
    # def set_attribs(self, in_dict):
    #     self.number = int(in_dict['number'])
    #     self.name = in_dict['name']
    #     self.age = int(in_dict['age'])
    #     self.gender = in_dict['gender']
    #     self.russian_sitizenship = bool(in_dict['russian_sitizenship'])