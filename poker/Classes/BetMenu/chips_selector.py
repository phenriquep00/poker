from poker.Classes.Buttons.buttons import Button
from poker.functions import COLOR


class ChipsSelector:
    """
    Menu for selecting amount of chips
    """
    def __init__(self, surf):
        """

        :param surf: pygame display object
        """
        self.surf = surf
        self.amount = 0
        self.active = False
        self.add = Button(self.surf, COLOR.dark_gray3, 800, 480, 50, 30, 'add', 'p')
        self.sub = Button(self.surf, COLOR.dark_gray3, 670, 480, 50, 30, 'sub', 'p')
        self.min = Button(self.surf, COLOR.dark_gray3, 620, 480, 50, 30, 'min', 'p')
        self.max = Button(self.surf, COLOR.dark_gray3, 850, 480, 50, 30, 'max', 'p')
        self.amount_display = Button(self.surf, COLOR.dark_gray1, 725, 480, 70, 30, f'{self.amount}', 'p')

    def draw(self):
        """
        draws the chip menu in the surface object
        :return:
        None
        """
        self.add.draw()
        self.sub.draw()
        self.max.draw()
        self.min.draw()
        self.amount_display.draw()

    def open(self):
        """
        open the menu
        :return:
        None
        """
        self.active = True

    def close(self):
        """
        close the menu and set the amount of chips to zero
        :return:
        None
        """
        self.active = False
        self.amount = 0

    def add_chips(self, value=5):
        """
        add chips to the amount
        :param value: amount of chips to be added, standard value of 5
        :return:
        None
        """
        self.amount += value
        self.amount_display = Button(self.surf, COLOR.dark_gray1, 725, 480, 70, 30, f'{self.amount}', 'p')

    def sub_chips(self, value=5):
        """
        Subtract chips from the amount
        :param value: amount of chips to be subtracted, standard value of 5
        :return:
        None
        """
        if self.amount >= 0:
            self.amount -= value
            self.amount_display = Button(self.surf, COLOR.dark_gray1, 725, 480, 70, 30, f'{self.amount}', 'p')
