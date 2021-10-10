class single:
    def __init__(self, name='', released=2021, group=''):
        self.name=name
        self.group=group
        self.released=released
    
    def strPlain(self):
        return self.name+"\n"+self.group+"\n"+self.released.__str__()+"\n\n"
    
    def strWeb(self):
        return self.name+"<br />"+self.group+"<br />"+self.released.__str__()+"<br /><br />"
        
    def strFormatted(self):
        return "Сингл:\n"+"Название:{} Группа:{} Выпущен в:{}".format(self.name,self.group,self.released)
        
    def input(self):
        self.name=input("Имя:")
        self.group=input("Группа:")
        self.released=int(input("Выпущен в:"))