from single import single

class album(single):
    def __init__(self, name='', released=2021, group='', numSongs=1):
        self.name=name
        self.group=group
        self.released=released
        self.numSongs=numSongs
        
    def strPlain(self):
        return self.name+"\n"+self.group+"\n"+self.released.__str__()+"\n"+self.numSongs.__str__()+"\n\n"
    
    def strWeb(self):
        return self.name+"<br />"+self.group+"<br />"+self.released.__str__()+"<br />"+self.numSongs.__str__()+"<br /><br />"
        
    def strFormatted(self):
        return "Альбом:\n"+"Название:{} Группа:{} Выпущен в:{} Песен:{}".format(self.name,self.group,self.released,self.numSongs)
        
    def input(self):
        self.name=input("Имя:")
        self.group=input("Группа:")
        self.released=int(input("Выпущен в:"))
        self.numSongs=int(input("Число песен:"))