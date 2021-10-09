import pickle


class FileIO:
    @staticmethod
    def dump(arr):
        with open('asm2104/st13/dump.pickle', 'wb') as f:
            pickle.dump(arr, f)

    @staticmethod
    def load():
        with open('asm2104/st13/dump.pickle', 'rb') as f:
            return pickle.load(f)