from poker.functions import COLOR
from poker.Classes.Buttons.buttons import Button


class Configurations:
    def __init__(self, surface):
        """

        :param surface: pygame display object to be the surface where the configuration object will be displayed
        """
        self.surface = surface
        self.active = False
        self.back_button = Button(self.surface, COLOR.dark_gray3, 0, 0, 100, 100, 'Back', 'm')

    def draw(self):
        """
        fill the surface screen with the configs background, and draw the elements inside configrations
        :return:
        None
        """
        self.surface.fill(COLOR.black)
        self.back_button.draw()

    def toggle_config(self):
        """
        toggle the configuration object attribute active to whether draw or not the configuration object over the
        surface
        :return:
        None
        """
        if self.active:
            self.active = False
        else:
            self.active = True
