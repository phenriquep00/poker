import pygame
from poker.functions import COLOR


class CardCombination:
    def __init__(self, surf, X, Y, wid, hei):
        self.active = False
        self.surf = surf
        self.coordinates = (X, Y)
        self.size = (wid, hei)

    def toggle(self):
        self.active = not self.active

    def draw(self):
        if self.active:
            pygame.draw.rect(self.surf, COLOR.black, [self.coordinates, self.size], border_radius=5)
