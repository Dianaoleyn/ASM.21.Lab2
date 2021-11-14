import pickle


class FileStrategy:
    @staticmethod
    def dump(array):
        with open('asm2104/st09/save.pickle', 'wb') as f:
            pickle.dump(array, f)

    @staticmethod
    def load():
        with open('asm2104/st09/save.pickle', 'rb') as f:
            return pickle.load(f)
