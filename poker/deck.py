import pygame
import os


class Deck:
    # TODO: shuffle deck method
    def __init__(self):
        self.clubs = [Card(image=f'{_}.png', value=_, suit='clubs') for _ in range(2, 15)]
        self.diamonds = [Card(image=f'{_}.png', value=_, suit='diamonds') for _ in range(2, 15)]
        self.hearts = [Card(image=f'{_}.png', value=_, suit='hearts') for _ in range(2, 15)]
        self.spades = [Card(image=f'{_}.png', value=_, suit='spades') for _ in range(2, 15)]


class Card:
    # Each card will have a image attribute (from pics) and a value
    def __init__(self, image, value, suit):
        self.image = pygame.image.load(os.path.join('pics', f'{suit}', f'{image}'))
        self.value = value
        self.suit = suit
