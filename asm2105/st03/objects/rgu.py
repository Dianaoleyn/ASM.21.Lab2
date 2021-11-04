
class rgu:
    def __init__(self, storage):
        self.name='РГУ нефти и газа'
        self.members={}
        self.storage=storage()

        try:
            self.load()
        except:pass

    def save(self):
        self.storage.save([self.members, self.name])

    def load(self):
        try:
            [self.members, self.name]=self.storage.load()
        except:pass

    def append(self, member):
        member.id=len(self.members)
        self.members[member.id]=member

    def search_by_name(self, name):
        for member in self.members.values():
            if member.name==name:
                return member

    def search_by_id(self, id):
        if int(id) in self.members:
            return self.members[int(id)]

    def clear(self):
        self.members.clear()

