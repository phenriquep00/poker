class Player:
    def __init__(self, name):
        self.hand = []
        self.chips = 500
        self.bet_chips = 0
        self.name = name
        self.action = True
        self.rank = 0
        self.value = ''
        self.win = False

    def bet(self, amount):
        # TODO: every time a bot make a bet, use the bet_animate function to animate it
        if self.chips == 0:
            pass
        else:
            self.chips -= amount
            self.bet_chips = amount
        return amount

    def fold(self):
        pass

    def set_name(self, new_name):
        self.name = new_name
