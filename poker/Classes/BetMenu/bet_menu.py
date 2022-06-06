from poker.Classes.Buttons.buttons import Button
from poker.functions import COLOR


class BetMenu:
    def __init__(self, surf):
        self.surf = surf
        self.bet_btn = Button(self.surf, COLOR.dark_blue3, 630, 520, 85, 50, 'BET', 'm')
        self.pass_btn = Button(self.surf, COLOR.dark_blue2, 720, 520, 85, 50, 'PASS', 'm')
        self.fold_btn = Button(self.surf, COLOR.dark_blue1, 810, 520, 85, 50, 'FOLD', 'm')

    def draw(self):
        self.bet_btn.draw()
        self.pass_btn.draw()
        self.fold_btn.draw()
