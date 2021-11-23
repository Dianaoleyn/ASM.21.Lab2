class InputStrategy:
    def input(newElement,__dict__):
            newElement.name = __dict__['name']
            newElement.surname = __dict__['surname']
            newElement.age = __dict__['age']
            newElement.mark = __dict__['mark']
            if __dict__.__contains__('grant'):
                newElement.grant=__dict__['grant']
            if __dict__.__contains__('number'):
                newElement.number=__dict__['number']