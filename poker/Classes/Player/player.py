

class Player:
    def __init__(self, name):
        """
        Player objects to gather all player's data and actions
        :param name: player's name
        """
        self.hand = []
        self.chips = 500
        self.name = name
        self.active = False

    def bet(self, amount):
        if self.active:
            self.chips -= amount
            return amount

    def turn(self):
        self.active = True


class Bot(Player):
    def __init__(self, name):
        super().__init__(name)
