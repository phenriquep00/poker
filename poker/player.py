class Player:
    def __init__(self):
        self.hand = []
        self.chips = 500
        self.name = 'player'
        self.small = True
        self.action = True

    def bet(self, amount):
        if self.chips == 0:
            pass
        else:
            self.chips -= amount
        return amount

    def fold(self):
        pass

    def set_name(self, new_name):
        self.name = new_name
