from flask import render_template

from StorageIO import Pickle
from ConsoleIO import ConsoleIO
from Html import Html


class Team:

    def __init__(self, storage_strategy=Pickle, strategy=Pickle, html=Html()):
        self.storage_strategy = storage_strategy
        self.strategy = strategy
        self.html = html

        try:
            self.load()
            self.maxid = int(max(self.members.keys()))
        except:
            self.members = {}
            self.maxid = 0

    def change_strategy(self):
        strategy_list = [
            {'text': 'Pickle', 'class': Pickle},
            {'text': 'Console', 'class': ConsoleIO},
            {'text': 'HTML', 'class': Html}
        ]

        return render_template('change_strategy.html', classes=strategy_list)

    def index(self):
        return render_template('show.html', members=self.members)

    def load(self):
        self.members = self.strategy.load()

    def dump(self):
        return self.strategy.dump(self.members)

    def add_member(self):
        if self.strategy == ConsoleIO:
            item = ConsoleIO.load()
            self.maxid += 1
            item.id = self.maxid
            self.members[item.id] = item
        else:
            item = self.html.load()
            self.maxid += 1
            item.id = self.maxid
            self.members[item.id] = item

    def delete_all(self):
        self.members.clear()
        self.maxid = 0

    def delete_member(self, id):
        del self.members[id]

    def edit_member(self, id):
        item = self.html.load()
        item.id = id
        self.members[id] = item
