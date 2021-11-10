from Adaptation import Adaptation

class Original:
    def __init__(self, name='', genre='', episodenum=1):
        self.name=name
        self.genre=genre
        self.episodenum=episodenum
        
    def strSimple(self):
        return self.name+"\n"+self.genre+"\n"+"\n"+self.episodenum.__str__()+"\n\n"
    
    def strWeb(self):
        return self.name+"<br />"+self.genre+"<br />"+"<br />"+self.episodenum.__str__()+"<br /><br />"
        
    def strEditing(self):
        return "Сериал:\n"+"Название:{} Жанр:{} Количество серий:{} ".format(self.name,self.genre,self.episodenum,)
        
    def input(self):
        self.name=input("Имя:")
        self.genre=input("Жанр:")
        self.episodenum=int(input("Количество эпизодов:"))