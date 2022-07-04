from poker.functions import COLOR
from poker.Classes.Buttons.buttons import Button
from poker.Classes.Labels.labels import Label


# TODO: Add a option to change the player and the bot's names
class Configurations:
    def __init__(self, surface):
        """

        :param surface: pygame display object to be the surface where the configuration object will be displayed
        """
        self.surface = surface
        self.active = False

        self.is_sound_on = True

        self.back_button = Button(self.surface, COLOR.dark_gray3, 0, 0, 100, 60, 'Back', 'm')
        self.sound_label = Label(self.surface, 100, 100, 'SoundFX: ', 'g')
        self.sound_button_on = Button(self.surface, COLOR.green, 300, 90, 70, 60, 'ON', 'm')
        self.sound_button_off = Button(self.surface, COLOR.dark_gray1, 380, 90, 80, 60, 'OFF', 'm')

    def draw(self):
        """
        fill the surface screen with the configs background, and draw the elements inside configurations
        :return:
        None
        """
        self.surface.fill(COLOR.black)
        self.back_button.draw()
        self.sound_label.draw()
        self.sound_button_on.draw()
        self.sound_button_off.draw()

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
