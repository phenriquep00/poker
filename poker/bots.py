class Bot:
    def __init__(self):
        self.hand = []
        self.chips = 500
        self.bet_chips = 0

    def do(self):
        # TODO: analyse the table and the bot's chances to win, then, do the most valuable action.
        amount = 40
        self.bet(amount)

    def bet(self, amount):
        if self.chips == 0:
            pass
        else:
            self.chips -= amount
            self.bet_chips = amount
        return amount


class Table:
    def __init__(self):
        self.cards = []
        self.pot = 0

    def get_chips(self, amount):
        self.pot += amount
