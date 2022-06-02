from poker.Classes.Buttons.buttons import Button
from poker.functions import COLOR


class ChipsSelector:
    def __init__(self, surf):
        self.surf = surf
        self.amount = 0
        self.active = False
        self.add = Button(self.surf, COLOR.dark_gray3, 800, 480, 50, 30, 'add', 'p')
        self.sub = Button(self.surf, COLOR.dark_gray3, 670, 480, 50, 30, 'sub', 'p')
        self.min = Button(self.surf, COLOR.dark_gray3, 620, 480, 50, 30, 'min', 'p')
        self.max = Button(self.surf, COLOR.dark_gray3, 850, 480, 50, 30, 'max', 'p')
        self.amount_display = Button(self.surf, COLOR.dark_gray1, 725, 480, 70, 30, f'{self.amount}', 'p')

    def draw(self):
        self.add.draw()
        self.sub.draw()
        self.max.draw()
        self.min.draw()
        self.amount_display.draw()

    def open(self):
        self.active = True

    def close(self):
        self.active = False
        self.amount = 0

    def add_chips(self, value=5):
        self.amount += value
        self.amount_display = Button(self.surf, COLOR.dark_gray1, 725, 480, 70, 30, f'{self.amount}', 'p')

    def sub_chips(self, value=5):
        if self.amount >= 0:
            self.amount -= value
            self.amount_display = Button(self.surf, COLOR.dark_gray1, 725, 480, 70, 30, f'{self.amount}', 'p')
