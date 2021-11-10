from Adaptation import Adaptation
from Original import Original

import pickle

class Simple():
    def print(self, List):
        for i in List:
            print(i.strSimple())
            
class Editing():
    def print(self, List):
        for i in List:
            print(i.strEditing())
            
class PickleDump():
    def print(self, List):
        with open('data_pickle.io','wb') as f:
            pickle.dump(List,f)
            
class PickleLoad():
    def print(self, List):
        with open('data_pickle.io','rb') as f:
            return pickle.load(f)
        
class Web():
    def print(self, List):
        str=''
        for i in List:
            str+=i.strWeb()
        return str