class Player:
    def __init__(self, name):
        self.hand = []
        self.chips = 500
        self.name = name


class Bot(Player):
    def __init__(self, name):
        super().__init__(name)


