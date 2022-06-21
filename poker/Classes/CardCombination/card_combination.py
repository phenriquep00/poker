import pygame
from poker.functions import COLOR
from poker.Classes.Buttons.buttons import Button


class CardCombination:
    def __init__(self, surf, X, Y, wid, hei):
        self.active = False
        self.surf = surf
        self.coordinates = (X, Y)
        self.size = (wid, hei)
        self.close_button = Button(
            self.surf,
            COLOR.black,
            self.coordinates[0] + (self.size[0] - 60),
            self.coordinates[1] + 15,
            50,
            50,
            'X',
            'm'
        )

    def toggle(self):
        self.active = not self.active

    def draw(self):
        # window
        pygame.draw.rect(self.surf, COLOR.black, [self.coordinates, self.size], border_radius=5)
        # close button
        self.close_button.draw()
