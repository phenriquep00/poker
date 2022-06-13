from poker.Classes.Player.player import Player


# TODO: make a action based on the evaluation of the hand
class Bot(Player):
    def __init__(self, name):
        super().__init__(name)

    def evaluate(self, minimum):
        pass
