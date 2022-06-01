from poker.functions import COLOR
from poker.Classes.Buttons.buttons import Button


class Configurations:
    def __init__(self, surface):

        self.surface = surface
        self.active = False
        self.back_button = Button(self.surface, COLOR.dark_gray3, 0, 0, 100, 100, 'Back', 'm')

    def draw(self):
        self.surface.fill(COLOR.black)
        self.back_button.draw()

    def toggle_config(self):
        """
        change the active attribute to True to allow the config window to be initialized
        :return:
        None
        """
        if self.active:
            self.active = False
        else:
            self.active = True
