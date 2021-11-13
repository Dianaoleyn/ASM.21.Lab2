import pickle


class FileIO:
    @staticmethod
    def dump(mass):
        with open('asm2104/st12/list.pickle', 'wb') as f:
            pickle.dump(mass, f)

    @staticmethod
    def load():
        with open('asm2104/st12/list.pickle', 'rb') as f:
            return pickle.load(f)