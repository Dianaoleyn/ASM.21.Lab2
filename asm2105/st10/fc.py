class FC:
    footballers = []

    def __init__(self):
        pass

    def clearAll(self):
        self.footballers.clear()

    def write(self, strategy):
        return self.footballers.extend(strategy.load())

    def read(self, strategy):
        return strategy.dump(self.footballers)
