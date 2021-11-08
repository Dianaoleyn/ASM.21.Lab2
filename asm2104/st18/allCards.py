class allCards:
    def __init__(self):
        self.users=list()


    def store(self, strategy):
        strategy().store(self)

    def load(self, strategy):
        self.__dict__.update(strategy().load().__dict__)

    def add_member(self, element):
        element.id=len(self.users)
        self.users.append(element)
        return element.id

    def get_member(self, item):
        result=[]
        for member in self.users:
            try:
                if int(item)==member.id:
                    return member
            except:
                if item==member.name:
                    result.append(member)
        return result

    def clr(self):
        self.users.clear()