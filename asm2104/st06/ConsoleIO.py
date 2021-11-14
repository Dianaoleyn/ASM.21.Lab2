from Manager import Manager
from Player import Player
from Staff import Staff

member_type = {
    1: ('Add player', Player),
    2: ('Add staff', Staff),
    3: ('Add Manager', Manager)
}


class ConsoleIO:

    @staticmethod
    def dump(dict):
        for key, member in dict.items():
            print(member)
            print('________________\n')

    @staticmethod
    def load():
        print('Choose member you want to add:')
        for i, item in member_type.items():
            print(i, ": ", item[0])
        print("------------------------------")
        s = int(input())
        m = member_type[s][1]()
        return m




    # def edit_member(list):
    #     print('Choose member to edit:')
    #     edit_num = int(input())
    #     for i, item in member_type.items():
    #         print(i, ": ", item[0])
    #     print("------------------------------")
    #     sel = int(input())
    #     list.pop(edit_num)
    #     list.insert(edit_num, member_type[sel][1]())
    #     return list
