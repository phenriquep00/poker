import os
import pygame

from poker.functions import blit_rotate_center
from poker.Classes.Cards.cards import Deck
from poker.Classes.Player.player import Player
from poker.Classes.Player.player import Bot
from poker.Classes.Table.table import Table
from poker.Classes.Labels.labels import Label
from poker.Classes.BetMenu.bet_menu import BetMenu
from poker.Classes.BetMenu.chips_selector import ChipsSelector


class Game:
    """
    A game object that holds the occurrence of the game, the table, the deck, the cards, the players the bots and the
    chips
    """
    def __init__(self, surf):
        """
        :param: surf: surface where the game object will be created
        """
        self.surf = surf
        self.background = pygame.image.load(os.path.join('pics', 'poker_background.jpeg'))
        self.active = False

        self.deck = Deck()
        self.player = Player('User')
        self.table = Table()
        self.bot1 = Bot('Bot1')
        self.bot2 = Bot('Bot2')
        self.bot3 = Bot('Bot3')
        self.chip_img = pygame.image.load(os.path.join('pics', 'bet-img.png'))

        self.bet_menu = BetMenu(self.surf)
        self.chip_selector = ChipsSelector(self.surf)

        self.first_actions()

    def start_game(self):
        """
        change the active attribute to True to allow the game to be initialized
        :return:
        None
        """
        self.active = True

    def draw(self):
        """
        If game's active attribute is set to True, this function draws the game images on the window surface
        :return:
        None
        """
        if self.active:
            self.surf.blit(self.background, (0, 0))

            # player draw
            # player's name
            player_name = Label(self.surf, 400, 470, f'{self.player.name}', 'm')
            player_name.draw()
            # player's cards
            self.surf.blit(self.player.hand[0].image, (380, 500))
            self.surf.blit(self.player.hand[1].image, (420, 500))
            # player's chips
            self.surf.blit(self.chip_img, (500, 560))   # chip image
            player_chip = Label(self.surf, 535, 570, f'{self.player.chips}', 'p')
            player_chip.draw()

            # bots' draw
            # bot1
            # name
            bot1_name = Label(self.surf, 72, 300, f'{self.bot1.name}', 'm', 270)
            bot1_name.draw()
            # bot1 cards
            blit_rotate_center(self.surf, self.bot1.hand[0].image_back, (0, 240), 90)
            blit_rotate_center(self.surf, self.bot1.hand[1].image_back, (0, 280), 90)
            # bot1 chips
            self.surf.blit(self.chip_img, (0, 220))     # chip's image
            bot1_chip = Label(self.surf, 35, 230, f'{self.bot1.chips}', 'p')
            bot1_chip.draw()

            # bot2
            # name
            bot2_name = Label(self.surf, 410, 100, f'{self.bot2.name}', 'm', 180)
            bot2_name.draw()
            # bot2 cards
            self.surf.blit(self.bot2.hand[0].image_back, (380, 0))
            self.surf.blit(self.bot2.hand[1].image_back, (420, 0))
            # bot2 chips
            self.surf.blit(self.chip_img, (490, 0))     # chip's image
            bot2_chip = Label(self.surf, 525, 10, f'{self.bot2.chips}', 'p')
            bot2_chip.draw()

            # bot3
            # name
            bot3_name = Label(self.surf, 760, 300, f'{self.bot3.name}', 'm', 90)
            bot3_name.draw()
            # bot3 cards
            blit_rotate_center(self.surf, self.bot3.hand[0].image_back, (811, 240), 90)
            blit_rotate_center(self.surf, self.bot3.hand[1].image_back, (811, 280), 90)
            # bot3 chips
            self.surf.blit(self.chip_img, (801, 220))
            bot3_chip = Label(self.surf, 836, 230, f'{self.bot3.chips}', 'p')
            bot3_chip.draw()

            # bet menu
            self.bet_menu.draw()
            if self.chip_selector.active:
                self.chip_selector.draw()

    def first_actions(self):
        """
        Make the initial configurations to the game object:
            - Shuffles the deck
            - Give the cards to the Table object
            - give two cards to each player
        :return:
        None
        """
        # first action
        # shuffle deck
        self.deck.shuffle()
        # give cards
        # table cards
        self.table.cards = self.deck.give_table_cards()
        # players' cards (bots included)
        for _ in [self.player, self.bot1, self.bot2, self.bot3]:
            _.hand = self.deck.give_cards()
