import pickle


class FileOutputPickle:
    def do_input(self):
        with open('aam2107/st04/data.pickle', 'rb') as f:
            return pickle.load(f)

    def do_output(self, data):
        with open('aam2107/st04/data.pickle', 'wb') as f:
            pickle.dump(data, f)
