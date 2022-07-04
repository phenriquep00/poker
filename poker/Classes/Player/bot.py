from poker.Classes.Player.player import Player


# TODO: make a action based on the evaluation of the hand
class Bot(Player):
    def __init__(self, name):
        super().__init__(name)

    def evaluate(self, minimum):
        # TODO: make this function return a value between 0 and 1, the closer to 1, the greater is the chance to win
        pass


