import pickle


class File:
    def getEmployees(self):
        with open('asm2104/st15/dump.pickle', 'rb') as f:
            return pickle.load(f)

    def showEmployees(self, employees):
        with open('asm2104/st15/dump.pickle', 'wb') as f:
            pickle.dump(employees, f)
