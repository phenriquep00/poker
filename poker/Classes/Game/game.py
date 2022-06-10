import os
import pygame
# import random

from poker.functions import blit_rotate_center, COLOR, RANKING
from poker.Classes.Cards.cards import Deck
from poker.Classes.Player.player import Player
from poker.Classes.Player.bot import Bot
from poker.Classes.Table.table import Table
from poker.Classes.Labels.labels import Label
from poker.Classes.BetMenu.bet_menu import BetMenu
from poker.Classes.BetMenu.chips_selector import ChipsSelector
from poker.Classes.GameMenu.game_menu import GameMenu
from poker.Classes.Analyzer.win_analyzer import WinAnalyzer
from poker.Classes.Buttons.buttons import Button


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
        self.round = 0

        self.deck = Deck()
        self.player = Player('Player')
        self.table = Table()
        self.bot1 = Bot('Bot1')
        self.bot2 = Bot('Bot2')
        self.bot3 = Bot('Bot3')
        self.chip_img = pygame.image.load(os.path.join('pics', 'bet-img.png'))

        self.bet_menu = BetMenu(self.surf)
        self.game_menu = GameMenu(self.surf)
        self.chip_selector = ChipsSelector(self.surf)

        self.players = [self.player, self.bot1, self.bot2, self.bot3]

        # self.small = random.choice(self.players)
        # self.big = self.players[self.players.index(self.small) + 1] if self.small != self.bot3 else self.players[0]

        self.small = self.player
        self.big = self.bot1

        self.min = 10

        self.__first_actions()

        self.winner = Player
        self.end_btn = Button(self.surf, COLOR.dark_blue2, 720, 520, 85, 50, 'NEXT', 'm')

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

            # small & big symbols
            small = Label(self.surf, 0, 0, 'S', 'm', color=COLOR.yellow)
            big = Label(self.surf, 0, 0, 'B', 'm', color=COLOR.yellow)
            # change small & big symbol position according to whom is the small bet
            if self.small == self.player:
                small.move(360, 500)
                big.move(5, 365)
            elif self.small == self.bot1:
                small.move(5, 365)
                big.move(360, 5)
            elif self.small == self.bot2:
                small.move(360, 5)
                big.move(870, 365)
            elif self.small == self.bot3:
                small.move(870, 365)
                big.move(360, 500)

            small.draw()
            big.draw()

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

            # pot
            self.surf.blit(self.chip_img, (405, 350))
            pot = Label(self.surf, 440, 360, f'{self.table.pot}', 'p')
            pot.draw()

            # bet menu
            if self.round < 4:
                if self.player.active:
                    self.bet_menu.draw()
                    if self.chip_selector.active:
                        self.chip_selector.draw()
            else:
                # reveal the bot's cards
                # bot1 cards
                blit_rotate_center(self.surf, self.bot1.hand[0].image, (0, 240), 90)
                blit_rotate_center(self.surf, self.bot1.hand[1].image, (0, 280), 90)

                # bot2 cards
                self.surf.blit(self.bot2.hand[0].image, (380, 0))
                self.surf.blit(self.bot2.hand[1].image, (420, 0))

                # bot3 cards
                blit_rotate_center(self.surf, self.bot3.hand[0].image, (811, 240), 90)
                blit_rotate_center(self.surf, self.bot3.hand[1].image, (811, 280), 90)

                self.winner = self.get_winner()
                winner_text = Label(self.surf, 200, 200, f'Winner: {self.winner.name} with {self.winner.rank[0]}', 'm')
                winner_text.draw()

                self.end_btn.draw()

            # game menu
            self.game_menu.draw()

            # table cards
            coordinates = [(200, 230), (300, 230), (400, 230), (500, 230), (600, 230)]

            if self.round == 1:
                for _ in range(3):
                    self.surf.blit(self.table.cards[_].image, coordinates[_])
            elif self.round == 2:
                for _ in range(4):
                    self.surf.blit(self.table.cards[_].image, coordinates[_])
            elif self.round >= 3:
                for _ in range(5):
                    self.surf.blit(self.table.cards[_].image, coordinates[_])

    def __first_actions(self):
        """
        Make the initial configurations to the game object:
            - Shuffles the deck
            - Give the cards to the Table object
            - give two cards to each player
        :return:
        None
        """
        self.round = 0
        # first action
        # shuffle deck
        self.deck.shuffle()
        # give cards
        # table cards
        self.table.cards = self.deck.give_table_cards()
        # players' cards (bots included)
        for _ in [self.player, self.bot1, self.bot2, self.bot3]:
            _.hand = self.deck.give_cards()
            _.active = False

        self.small.active = True
        self.min = 10

    def next(self):
        """
        Loop through all the players to change the currently active player, given the action to the next player on the
        list who has the .playing attribute set to True
        :return:
        None
        """
        for player in self.players:
            if player.active:
                if player.name == self.player.name:
                    player.active = False
                    if self.bot1.playing:
                        self.bot1.active = True
                    elif self.bot2.playing:
                        self.bot2.active = True
                    else:
                        self.bot3.active = True
                    break
                elif player.name == self.bot1.name:
                    player.active = False
                    if self.bot2.playing:
                        self.bot2.active = True
                    elif self.bot3.playing:
                        self.bot3.active = True
                    else:
                        self.player.active = True
                    break
                elif player.name == self.bot2.name:
                    player.active = False
                    if self.bot3.playing:
                        self.bot3.active = True
                    elif self.player.playing:
                        self.player.active = True
                    else:
                        self.bot1.active = True
                    break
                elif player.name == self.bot3.name:
                    player.active = False
                    if self.player.playing:
                        self.player.active = True
                    elif self.bot1.playing:
                        self.bot1.active = True
                    else:
                        self.bot2.active = True
                    break

    def next_round(self):
        self.round += 1
        self.min = 0
        for _ in self.players:
            if _ == self.small:
                _.active = True
            else:
                _. active = False
            _.done = False

    def get_winner(self):
        rank = RANKING
        win_analyzer = WinAnalyzer(self.table.cards)
        # evaluate all hands
        self.player.rank = win_analyzer.evaluate(win_analyzer.order_hand(self.player))
        self.bot1.rank = win_analyzer.evaluate(win_analyzer.order_hand(self.bot1))
        self.bot2.rank = win_analyzer.evaluate(win_analyzer.order_hand(self.bot2))
        self.bot3.rank = win_analyzer.evaluate(win_analyzer.order_hand(self.bot3))

        for k, v in rank.items():
            for player in self.players:
                if player.rank[0] == k:
                    rank[k].append(player)

        for k, v in rank.items():
            if len(rank[k]) != 0:
                return rank[k][0]

    def end_round(self):
        self.winner.chips += self.table.pot
        self.table.pot = 0

        self.deck.reset()
        for player in self.players:
            player.reset_hand()

        self.__first_actions()
