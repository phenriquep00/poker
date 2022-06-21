from poker.functions import COLOR
from poker.Classes.Buttons.buttons import Button


class GameMenu:
    """
    Menu for game options ( restart, exit, check card combinations )
    """
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
        self.menu = Button(self.surf, COLOR.black, 0, 0, 230, 230, border=False)
        self.card_combination_button = Button(self.surf, COLOR.black, 20, 50, 200, 50, 'Combinations', 'm')
        self.restart_button = Button(self.surf, COLOR.black, 20, 110, 200, 50, 'Restart', 'm')
        self.exit_button = Button(self.surf, COLOR.black, 20, 170, 200, 50, 'Exit', 'm')

    def draw(self):
        if self.active:
            self.menu.draw()
            self.card_combination_button.draw()
            self.restart_button.draw()
            self.exit_button.draw()

        self.bg.draw()
        for button in self.buttons:
            button.draw()

    def toggle(self):
        self.active = not self.active
