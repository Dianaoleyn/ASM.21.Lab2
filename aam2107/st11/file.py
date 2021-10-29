import pickle


class File:
    def getEmployees(self):
        with open('aam2107/st11/dump.pickle', 'rb') as f:
            return pickle.load(f)

    def showEmployees(self, employees):
        with open('aam2107/st11/dump.pickle', 'wb') as f:
            pickle.dump(employees, f)
