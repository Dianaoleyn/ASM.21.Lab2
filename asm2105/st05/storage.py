import pickle


class Storage:
    def save(self, data):
        pass

    def load(self):
        pass


class LocalStorage(Storage):
    def save(self, data):
        with open('asm2105/st05/dm.db', 'wb') as file:
            pickle.dump(data, file)

    def load(self):
        try:
            with open('asm2105/st05/dm.db', 'rb') as file:
                return pickle.load(file)
        except EOFError:
            return []
