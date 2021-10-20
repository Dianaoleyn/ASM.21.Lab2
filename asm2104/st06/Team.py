from flask import render_template

import StorageIO
from ConsoleIO import ConsoleIO
from Html import Html


class Team:

    def __init__(self, storage_strategy=StorageIO.Pickle, strategy=ConsoleIO, html=Html(), members=[]):
        self.members = members
        self.storage_strategy = storage_strategy
        self.strategy = strategy
        self.html = html

    # def change_storage_strategy(self):
    #     storage_strategy_list = [
    #         {'text': 'Pickle', 'class': StorageIO.Pickle},
    #         {'text': 'Shelve', 'class': StorageIO.Shelve},
    #     ]
    #     return render_template('change_storage_strategy.html', classes=storage_strategy_list)

    def change_strategy(self):
        strategy_list = [
            {'text': 'Pickle', 'class': StorageIO.Pickle},
            {'text': 'Shelve', 'class': StorageIO.Shelve},
            {'text': 'Console', 'class': ConsoleIO},
            {'text': 'HTML', 'class': Html}
        ]

        return render_template('change_strategy.html', classes=strategy_list)

    def index(self):
        return render_template('show.html', members=self.members)

    def load(self):
        self.members = self.strategy.load(self.members)

    def dump(self):
        return self.strategy.dump(self.members)

    def add_member(self):
        self.members.append(self.html.load(list))

    def delete_members(self):
        self.members.clear()

    # def edit_member(self):
    #     self.members = edit_member(self.members)
