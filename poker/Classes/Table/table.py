class Table:
    def __init__(self):
        self.cards = []
        self.pot = 0

    def get_chips(self, amount):
        self.pot += amount

