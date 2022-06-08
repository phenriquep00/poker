from poker.Classes.Player.player import Player


class Bot(Player):
    def __init__(self, name):
        super().__init__(name)

    def evaluate(self, minimum):
        pass
