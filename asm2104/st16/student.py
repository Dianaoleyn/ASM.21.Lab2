from zapis import zapis

class student(zapis):
    def __init__(self):
        zapis.__init__(self)
        self.group=''
        self.course=int()

    def __str__(self):
        result=super().__str__()
        result+=f'Group: {self.group}\n' \
                f'Course: {self.course}\n'
        return result