import os
import pygame


class Game:
    def __init__(self, surf):
        self.surf = surf
        self.background = pygame.image.load(os.path.join('pics', 'poker_background.jpeg'))
        self.active = False

    def start_game(self):
        self.active = True

    def draw(self):
        self.surf.blit(self.background, (0, 0))
