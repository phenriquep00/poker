from test_game import TestGame


class WinAnalyzer:
    def __init__(self, table_cards, players):
        self.table_cards = table_cards
        self.players = players
        self.hands = dict()
        self.__order_hands()

    def __order_hands(self):
        for player in self.players:
            self.hands[player.name] = [self.__get_utils(player.hand[_]) for _ in range(2)]
            for _ in range(5):
                self.hands[player.name].append(self.__get_utils(self.table_cards[_]))

    @staticmethod
    def __get_utils(card):
        return card.value, card.suit


game = TestGame('surface')
an_test = WinAnalyzer(game.table.cards, game.players)
print(an_test.hands['Player'])
