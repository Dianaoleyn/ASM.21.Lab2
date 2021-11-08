import pickle

class Pickle:
    def store(self, obj):
        with open('store.db', 'wb') as file:
            pickle.dump(obj, file)

    def load(self):
        with open('store.db', 'rb') as file:
            return pickle.load(file)