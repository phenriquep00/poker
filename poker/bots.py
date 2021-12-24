class Bot:
    def __init__(self):
        self.hand = []
        self.chips = 500
        self.action = False
        self.next = False

    def do(self):
        if self.action:
            self.bet(40)
            self.action = False
            self.next = True

    def bet(self, amount):
        if self.chips == 0:
            pass
        else:
            self.chips -= amount
        return amount


class Table:
    def __init__(self):
        self.cards = []
        self.pot = 0

    def get_chips(self, amount):
        self.pot += amount
