import pickle


class Storage:
    def save(self, data):
        pass

    def load(self):
        pass


class LocalStorage(Storage):
    def save(self, data):
        with open('diana.db', 'wb') as file:
            pickle.dump(data, file)

    def load(self):
        with open('diana.db', 'rb') as file:
            return pickle.load(file)
