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

    def evaluate(self, hand):
        h, s, d, c = [], [], [], []
        for card in hand:
            # get amount of cards in every suit
            if card[1] in 'hearts':
                h.append(card)
            if card[1] in 'spades':
                s.append(card)
            if card[1] in 'diamonds':
                d.append(card)
            if card[1] in 'clubs':
                c.append(card)

            # flush possibilities
            for suit in [h, s, d, c]:
                if len(suit) >= 5:    # if true, there's a flush
                    # sorting
                    cards = sorted([suit[_][0] for _ in range(len(suit))], reverse=True)
                    # royal flush
                    if sum(cards[:5]) >= 60:
                        # if true, there's a royal flush
                        return 'royal flush'
                    # straight flush
                    elif cards[0] - 4 == cards[4]:
                        return 'straight flush'
                    else:
                        # flush
                        return 'flush'


game = TestGame('surface')
an_test = WinAnalyzer(game.table.cards, game.players)
test_hand = [(2, 'diamonds'), (3, 'diamonds'), (4, 'diamonds'), (5, 'diamonds'), (6, 'diamonds')]
print(an_test.evaluate(test_hand))
