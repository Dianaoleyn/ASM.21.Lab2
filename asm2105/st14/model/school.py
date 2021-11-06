
class school:
    def __init__(self, storage):
        self.list={}
        self.storage=storage()

        self.load()

    def save(self):
        self.storage.save(self.list)

    def load(self):
        try:
            self.list=self.storage.load()
        except: pass
        # print(self.list)

    def add(self, item):
        item.id=len(self.list)
        self.list[item.id]=item
        return item.id

    def clear(self):
        self.list.clear()

    def search(self, param):
        try:
            if int(param) in self.list:
                return self.list[int(param)]
            else:
                for item in self.list.values():
                    if str(item.name) == str(param):
                        return item
        except:
            for item in self.list.values():
                if str(item.name)==str(param):
                    return item
