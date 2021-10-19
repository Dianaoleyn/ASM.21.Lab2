import pickle
import shelve


class Pickle:
    @staticmethod
    def dump(array):
        with open('pickle_storage.pickle', 'wb') as f:
            pickle.dump(array, f)

    @staticmethod
    def load(listw):
        with open('pickle_storage.pickle', 'rb') as f:
            return pickle.load(f)


class Shelve:
    @staticmethod
    def dump(array):
        with shelve.open('shelve_storage') as f:
            f['key'] = array
            f.close()

    @staticmethod
    def load(listw):
        with shelve.open('shelve_storage') as f:
            return list(f['key'])
