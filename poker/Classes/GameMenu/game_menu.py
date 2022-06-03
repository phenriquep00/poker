from poker.functions import COLOR
from poker.Classes.Buttons.buttons import Button


class GameMenu:
    def __init__(self, surf):
        self.surf = surf
        self.active = False
        self.bg = Button(self.surf, COLOR.dark_red2, 0, 0, 40, 37)
        self.buttons = [
            Button(
                surf=self.surf,
                color=COLOR.white,
                X=7,
                Y=_,
                rectH=4,
                rectW=27,
                border=False
            )for _ in [8, 16, 24]
        ]
        self.menu = Button(self.surf, COLOR.black, 0, 0, 200, 300, border=False)

    def draw(self):
        if self.active:
            self.menu.draw()
        self.bg.draw()
        for button in self.buttons:
            button.draw()

    def toggle(self):
        if self.active:
            self.active = False
        else:
            self.active = True
