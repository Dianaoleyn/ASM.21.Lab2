class RGU:
    def __init__(self, storage):
        self.full_name='РГУ Нефти и газа им. М. И. Губкина'
        self.members= {}

        self.storage=storage()

        try:
            self.load()
        except:
            pass

    def load(self):
        # self.storage.load()
        # print('1', self.members)
        # print(self.storage.load())
        self.__dict__.update(self.storage.load())
        # print('2', self.members)

    def clear(self):
        self.members.clear()

    def get_by_num(self, num):
        if int(num) in self.members:
            return self.members[int(num)]
        else:
            return None

    def save(self):
        self.storage.save(self.__dict__)

    def add_member(self, member):
        member.number=len(self.members)
        self.members[member.number]=member

