class Player:
    def __init__(self):
        self.hand = []
        self.chips = 500
        self.name = 'player'

    def bet(self):
        if self.chips > 0:
            pass

    def fold(self):
        pass

    def set_name(self, new_name):
        self.name = new_name
