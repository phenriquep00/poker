import pygame
import os
import random


class Deck:
    """
    A deck object is constituted of 52 card objects, 13 of each nape
    """
    def __init__(self):
        self.clubs = [Card(image=f'{_}.png', value=_, suit='clubs') for _ in range(2, 15)]
        self.diamonds = [Card(image=f'{_}.png', value=_, suit='diamonds') for _ in range(2, 15)]
        self.hearts = [Card(image=f'{_}.png', value=_, suit='hearts') for _ in range(2, 15)]
        self.spades = [Card(image=f'{_}.png', value=_, suit='spades') for _ in range(2, 15)]
        self.deck = []

    def shuffle(self):
        """
        shuffles the order of the cards inside the self. deck list
        :return:
        None
        """
        for _ in [self.clubs, self.spades, self.hearts, self.diamonds]:
            for i in _:
                self.deck.append(i)

        random.shuffle(self.deck)

    def give_cards(self):
        """
        get the 2 top cards on the deck giving them away to a player
        :return:
        2 card objects
        """
        cards = []
        for _ in range(2):
            _ = self.deck[0]
            self.deck.pop(0)
            cards.append(_)
        return cards[0], cards[1]

    def give_table_cards(self):
        """
        get five cards and give them to the table object
        :return:
        5 card objects
        """
        cards = []
        for _ in range(5):
            _ = self.deck[0]
            self.deck.pop(0)
            cards.append(_)
        return cards[0], cards[1], cards[2], cards[3], cards[4]


class Card:
    """
    Generate cards to be used in the game
    """
    def __init__(self, image, value, suit):
        """

        :param image: image-like archive to be used as the card front
        :param value: number of the card, from 2 to 14
        :param suit: card's suit
        """
        self.image = pygame.image.load(os.path.join('pics', f'{suit}', f'{image}'))
        self.image_back = pygame.image.load(os.path.join('pics', 'card-back.png'))
        self.value = value
        self.suit = suit
