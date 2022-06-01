from poker.Classes.Colors.colors import Colors
from poker.Classes.Buttons.buttons import Button


colors = Colors()


class Configurations:
    def __init__(self, surface):

        self.surface = surface
        self.active = False
        self.back_button = Button(self.surface, colors.dark_gray3, 0, 0, 100, 100, 'Back', 'm')

    def draw(self):
        self.surface.fill(colors.black)
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


