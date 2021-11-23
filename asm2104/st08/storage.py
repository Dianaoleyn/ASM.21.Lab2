import pickle

class PickleStorage:
    def store(self, obj):
        with open('storage.db', 'wb') as file:
            pickle.dump(obj, file)

    def load(self):
        with open('storage.db', 'rb') as file:
            return pickle.load(file)
