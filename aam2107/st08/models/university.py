
class university:
    def __init__(self, storage):
        self.name='РГУ нефти и газа'
        self.items={}

        self.storage=storage()

        try:
            self.load()
        except:
            pass

    def dump(self):
        self.storage.dump(self.__dict__)

    def load(self):
        self.__dict__.update(self.storage.load())

    def addItem(self, item):
        item.id=len(self.items)
        self.items[item.id]=item

    def get_by_number(self, number):
        if int(number) in self.items:
            return self.items[int(number)]

    def get_by_name(self, name):
        for item in self.items.values():
            if item.name==name:
                return item

    def clear(self):
        self.items.clear()