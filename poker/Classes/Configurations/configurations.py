from poker.functions import COLOR
from poker.Classes.Buttons.buttons import Button
from poker.Classes.Labels.labels import Label
from poker.Classes.InputBox.input_box import InputBox


class Configurations:
    def __init__(self, surface):
        """

        :param surface: pygame display object to be the surface where the configuration object will be displayed
        """
        self.surface = surface
        self.active = False

        self.is_sound_on = True

        # elements
        # back button
        self.back_button = Button(self.surface, COLOR.dark_gray3, 0, 0, 100, 60, 'Back', 'm')
        # sound label
        self.sound_label = Label(self.surface, 100, 100, 'SoundFX: ', 'g')
        # sound ON option
        self.sound_button_on = Button(self.surface, COLOR.green, 300, 90, 70, 60, 'ON', 'm')
        # sound OFF option
        self.sound_button_off = Button(self.surface, COLOR.dark_gray1, 380, 90, 80, 60, 'OFF', 'm')
        # player name label
        self.player_name = Label(self.surface, 100, 200, 'Player Name: ', 'g')
        # player name input box
        self.player_name_input_box = InputBox(self.surface, 370, 180, 300, 80)

    def draw(self):
        """
        fill the surface screen with the configs background, and draw the elements inside configurations
        :return:
        None
        """
        self.surface.fill(COLOR.black)
        self.back_button.draw()

        # sound options
        self.sound_label.draw()
        self.sound_button_on.draw()
        self.sound_button_off.draw()

        # player name options
        self.player_name.draw()
        self.player_name_input_box.draw()

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
