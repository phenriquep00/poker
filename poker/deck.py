import pygame
import os
import random


class Deck:
    # TODO: shuffle deck method
    def __init__(self):
        self.clubs = [Card(image=f'{_}.png', value=_, suit='clubs') for _ in range(2, 15)]
        self.diamonds = [Card(image=f'{_}.png', value=_, suit='diamonds') for _ in range(2, 15)]
        self.hearts = [Card(image=f'{_}.png', value=_, suit='hearts') for _ in range(2, 15)]
        self.spades = [Card(image=f'{_}.png', value=_, suit='spades') for _ in range(2, 15)]
        self.deck = []

    def shuffle(self):
        for _ in [self.clubs, self.spades, self.hearts, self.diamonds]:
            for i in _:
                self.deck.append(i)

        random.shuffle(self.deck)


class Card:
    # Each card will have a image attribute (from pics) and a value
    def __init__(self, image, value, suit):
        self.image = pygame.image.load(os.path.join('pics', f'{suit}', f'{image}'))
        self.value = value
        self.suit = suit
