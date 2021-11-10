from Adaptation import Adaptation
from Original import Original
from Function import Simple, Editing, PickleDump, PickleLoad, Web

class AniList:
    def __init__(self):
        self.plan=Web()
        self.List=[]
        self.chosen='Web'
        
    def assignPlan(self):
        if self.chosen=='Editing':
            self.plan=Editing()
        if self.chosen=='Simple':
            self.plan=Simple()
        if self.chosen=='Web':
          self.plan=Web()
        
    def add(self):
        case = int(input("0 - Адаптация, 1  - Оригинал: \n"))
        entity = Original() if case else Adaptation()
        entity.input()
        self.List.append(entity)
        
    def add(self, entity):
        self.List.append(entity)
        
    def print(self):
        return self.plan.print(self.List)
        
    def clear(self):
        self.List.clear()
        
    def file_write(self):
        self.plan=PickleDump()
        self.plan.print(self.List)
        self.assignPlan()
    
    def file_read(self):
        self.plan=PickleLoad()
        self.List=self.plan.print(self.List)
        self.assignPlan()
    
    def delete(self, ind):
        self.List.pop(ind)
    
    def swapMode(self):
        if self.chosen=='Editing':
            self.chosen='Simple'
            self.assignPlan()
        else:
            self.chosen='Editing'
            self.assignPlan()
        
   