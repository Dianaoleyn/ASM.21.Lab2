
class container:
    def __init__(self):
        self.elements=list()


    def store(self, strategy):
        strategy().store(self)

    def load(self, strategy):
        # print(strategy().load().__dict__)
        self.__dict__.update(strategy().load().__dict__)
        # print(self.__dict__)

    def add_member(self, element):
        element.id=len(self.elements)
        self.elements.append(element)
        return element.id

    def get_member(self, item):
        result=[]
        for member in self.elements:
            try:
                if int(item)==member.id:
                    return member
            except:
                if item==member.name:
                    result.append(member)
        return result

    def clr(self):
        self.elements.clear()
