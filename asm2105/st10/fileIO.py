import pickle


class FileIO:
    @staticmethod
    def dump(array):
        with open('asm2105/st10/file', 'wb') as f:
            pickle.dump(array, f)

    @staticmethod
    def load():
        with open('asm2105/st10/file', 'rb') as f:
            return pickle.load(f)
