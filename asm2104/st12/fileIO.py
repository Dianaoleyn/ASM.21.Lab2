import pickle


class FileIO:
    @staticmethod
    def dump(mass):
        with open('list.pickle', 'wb') as f:
            pickle.dump(mass, f)

    @staticmethod
    def load():
        with open('list.pickle', 'rb') as f:
            return pickle.load(f)