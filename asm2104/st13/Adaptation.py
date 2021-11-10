class Adaptation:
    def __init__(self, name='', episodenum=24, genre=''):
        self.name = name
        self.genre = genre
        self.episodenum = episodenum

    def strSimple(self):
        return self.name + "\n" + self.genre + "\n" + self.episodenum.__str__() + "\n\n"

    def strWeb(self):
        return self.name+"<br />"+self.genre+"<br />"+self.episodenum.__str__()+"<br /><br />"

    def strEditing(self):
        return "Адаптация:\n" + "Название:{} Жанр:{} Количество серий:{}".format(self.name, self.genre, self.episodenum)

    def input(self):
        self.name = input("Название аниме сериала:")
        self.genre = input("Жанр:")
        self.episodenum = int(input("Количество серий:"))
