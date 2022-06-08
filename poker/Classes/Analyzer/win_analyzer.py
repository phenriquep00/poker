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

    @staticmethod
    def evaluate(hand):
        h, s, d, c = [], [], [], []

        occurrence = {}
        for i in range(2, 15):
            occurrence[i] = 0

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

                    else:
                        # straight flush
                        if cards[0] - 4 == cards[4]:
                            return 'straight flush'
                        elif len(cards) == 6 and cards[1] - 4 == cards[5]:
                            return 'straight flush'
                        elif len(cards) == 7 and cards[2] - 4 == cards[6]:
                            return 'straight flush'
                        else:
                            # flush
                            return 'flush'

            # pair matching
            for k, v in occurrence.items():
                if k == card[0]:
                    occurrence[k] += 1

        pair = 0
        three = 0
        four = 0
        for k, v in occurrence.items():
            if occurrence[k] == 2:  # there's a pair
                pair += 1
            elif occurrence[k] == 3:
                three += 1
            elif occurrence[k] == 4:
                four += 1

        if four >= 1:
            return 'four of a kind'
        elif three >= 1:
            if pair >= 1:
                return 'full house'
            else:
                return 'three of a kind'
        elif pair == 1:
            return 'one pair'
        elif pair >= 2:
            return 'two pair'

        cards = sorted([hand[_][0] for _ in range(len(hand))], reverse=True)
        if cards[0] - 4 == cards[4]:
            return 'straight'
        elif len(cards) >= 6 and cards[1] - 4 == cards[5]:
            return 'straight'
        elif len(cards) >= 7 and cards[2] - 4 == cards[6]:
            return 'straight'


game = TestGame('surface')
an_test = WinAnalyzer(game.table.cards, game.players)
test_hand = [(2, 'diamonds'), (3, 'spades'), (4, 'hearts'), (5, 'diamonds'), (6, 'diamonds'), (10, 'diamonds')]
print(an_test.evaluate(test_hand))
