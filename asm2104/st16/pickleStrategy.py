import pickle

class PickleStorage:
    def store(self, obj):
        with open('ASM18.db', 'wb') as file:
            pickle.dump(obj, file)

    def load(self):
        with open('ASM18.db', 'rb') as file:
            return pickle.load(file)
