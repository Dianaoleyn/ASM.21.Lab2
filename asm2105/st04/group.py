class Group:
    def __init__(self, strategy, storage):
        self.group_members = []
        self.strategy = strategy
        self.storage = storage()

    def add(self, student):
        student.id = len(self.group_members)
        student.set()
        self.group_members.append(student)

    def show(self):
        for student in self.group_members:
            student.get()

    def load(self):
        self.group_members = self.storage.load()

    def save(self):
        self.storage.save(self.group_members)

    def clear(self):
        self.group_members.clear()
