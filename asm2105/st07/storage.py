import pickle


class Storage:
    def save(self, data):
        pass

    def load(self):
        pass


class LocalStorage(Storage):
    def save(self, data):
        with open('asm2105/st07/zhurba.db', 'wb') as file:
            pickle.dump(data, file)

    def load(self):
        with open('asm2105/st07/zhurba.db', 'rb') as file:
            return pickle.load(file)
