import pickle


class File:

    @staticmethod
    def input(employee_list):
        with open('asm2104/st11/output.pickle', 'rb') as f:
            return pickle.load(f)

    @staticmethod
    def output(employee_list):
        with open('asm2104/st11/output.pickle', 'wb') as f:
            pickle.dump(employee_list, f)
