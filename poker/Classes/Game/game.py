import os
import pygame

from poker.Classes.Cards.cards import Deck
from poker.Classes.Player.player import Player
from poker.Classes.Player.player import Bot
from poker.Classes.Table.table import Table


# functions:
# function to rotate an image object around it's center
def blit_rotate_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect)


class Game:
    def __init__(self, surf):
        self.surf = surf
        self.background = pygame.image.load(os.path.join('pics', 'poker_background.jpeg'))
        self.active = False
        self.deck = Deck()
        self.player = Player('User')
        self.table = Table()
        self.bot1 = Bot('Bot1')
        self.bot2 = Bot('Bot2')
        self.bot3 = Bot('Bot3')
        self.first_actions()

    def start_game(self):
        self.active = True

    def draw(self):

        self.surf.blit(self.background, (0, 0))
        # player's cards
        self.surf.blit(self.player.hand[0].image, (380, 500))
        self.surf.blit(self.player.hand[1].image, (420, 500))

        # bots' cards

        # bot1
        blit_rotate_center(self.surf, self.bot1.hand[0].image_back, (0, 240), 90)
        blit_rotate_center(self.surf, self.bot1.hand[1].image_back, (0, 280), 90)

        # bot2
        self.surf.blit(self.bot2.hand[0].image_back, (380, 0))
        self.surf.blit(self.bot2.hand[1].image_back, (420, 0))

        # bot3
        blit_rotate_center(self.surf, self.bot3.hand[0].image_back, (811, 240), 90)
        blit_rotate_center(self.surf, self.bot3.hand[1].image_back, (811, 280), 90)

    def first_actions(self):
        # first action
        # shuffle deck
        self.deck.shuffle()
        # give cards
        # table cards
        self.table = self.deck.give_table_cards()
        # players' cards (bots included)
        for _ in [self.player, self.bot1, self.bot2, self.bot3]:
            _.hand = self.deck.give_cards()
