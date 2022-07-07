

class Player:
    chips = None

    def __init__(self, name):
        """
        Player objects to gather all player's data and actions
        :param name: player's name
        """
        self.hand = []
        self.chips = 500
        self.name = name
        self.display_name = ''
        self.playing = True
        self.active = False
        self.done = False
        self.rank = ''

    def bet(self, amount):
        if self.active and self.chips > 0:
            self.chips -= amount
            self.done = True
            return amount
        else:
            self.done = True
            return 0

    def turn(self):
        self.active = True

    def fold(self):
        self.playing = False

    def reset_hand(self):
        self.hand = []

    def reset_chips(self, amount=500):
        self.chips = amount

    def update_name(self, new_name):
        self.display_name = new_name
