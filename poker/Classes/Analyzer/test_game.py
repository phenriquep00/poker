import random
from poker.Classes.Player.player import Player
from poker.Classes.Player.bot import Bot
from poker.Classes.Table.table import Table


class TestGame:
    """
    A game object that holds the occurrence of the game, the table, the deck, the cards, the players the bots and the
    chips
    """
    def __init__(self, surf):
        """
        :param: surf: surface where the game object will be created
        """
        self.surf = surf
        self.active = False
        self.round = 0

        self.deck = TestDeck()
        self.player = Player('Player')
        self.table = Table()
        self.bot1 = Bot('Bot1')
        self.bot2 = Bot('Bot2')
        self.bot3 = Bot('Bot3')
        self.players = [self.player, self.bot1, self.bot2, self.bot3]
        self.__first_actions()

    def __first_actions(self):
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


class TestDeck:
    """
    A deck object is constituted of 52 card objects, 13 of each nape
    """
    def __init__(self):
        self.clubs = [TestCard(value=_, suit='clubs') for _ in range(2, 15)]
        self.diamonds = [TestCard(value=_, suit='diamonds') for _ in range(2, 15)]
        self.hearts = [TestCard(value=_, suit='hearts') for _ in range(2, 15)]
        self.spades = [TestCard(value=_, suit='spades') for _ in range(2, 15)]
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


class TestCard:
    """
    Generate cards to be used in the game
    """
    def __init__(self, value, suit):
        """
        :param value: number of the card, from 2 to 14
        :param suit: card's suit
        """

        self.value = value
        self.suit = suit
