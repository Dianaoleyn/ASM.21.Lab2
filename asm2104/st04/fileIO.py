import pickle


class FileIO:
    def addOneElement(self,newElement,newList):
        newList.append(newElement)
        with open('asm2104/st04/file.pickle', 'wb') as f:
            pickle.dump(newList, f)

    
    def output(self,newList):
        with open('asm2104/st04/file.pickle', 'wb') as f:
            pickle.dump(newList, f)

    def input(self,newList):
        with open('asm2104/st04/file.pickle', 'rb') as f:
            return newList+pickle.load(f)