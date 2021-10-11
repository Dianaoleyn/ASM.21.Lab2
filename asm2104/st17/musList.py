from single import single
from album import album
from strategies import Plain, Formatted, PickleDump, PickleLoad, Web

class musList:
    def __init__(self):
        self.strategy=Web()
        self.List=[]
        self.chosen='Web'
        
    def assignStrategy(self):
        if self.chosen=='Formatted':
            self.strategy=Formatted()
        if self.chosen=='Plain':
            self.strategy=Plain()
        if self.chosen=='Web':
          self.strategy=Web()
        
    def add(self):
        case = int(input("0 - сингл, 1  - альбом: \n"))
        entity = album() if case else single()
        entity.input()
        self.List.append(entity)
        
    def add(self, entity):
        self.List.append(entity)
        
    def print(self):
        return self.strategy.print(self.List)
        
    def clear(self):
        self.List.clear()
        
    def file_write(self):
        self.strategy=PickleDump()
        self.strategy.print(self.List)
        self.assignStrategy()
    
    def file_read(self):
        self.strategy=PickleLoad()
        self.List=self.strategy.print(self.List)
        self.assignStrategy()
    
    def delete(self, ind):
        self.List.pop(ind)
    
    def swapMode(self):
        if self.chosen=='Formatted':
            self.chosen='Plain'
            self.assignStrategy()
        else:
            self.chosen='Formatted'
            self.assignStrategy()
        
   