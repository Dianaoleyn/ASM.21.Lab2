from single import single
from album import album
import pickle
    
class Plain():
    def print(self, List):
        for i in List:
            print(i.strPlain())
            
class Formatted():
    def print(self, List):
        for i in List:
            print(i.strFormatted())
            
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