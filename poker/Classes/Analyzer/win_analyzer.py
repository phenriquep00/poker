class WinAnalyzer:
    def __init__(self, table_cards):
        self.table_cards = table_cards

    def order_hand(self, player):
        new_hand = [self.__get_utils(player.hand[_]) for _ in range(2)]
        for _ in range(5):
            new_hand.append(self.__get_utils(self.table_cards[_]))
        return new_hand

    @staticmethod
    def __get_utils(card):
        return card.value, card.suit

    @staticmethod
    def evaluate(hand):
        h, s, d, c = [], [], [], []

        total = sum(sorted([hand[_][0] for _ in range(len(hand))], reverse=True)[:5])

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
                        return 'royal flush', total

                    else:
                        # straight flush
                        if cards[0] - 4 == cards[4]:
                            return 'straight flush', total
                        elif len(cards) == 6 and cards[1] - 4 == cards[5]:
                            return 'straight flush', total
                        elif len(cards) == 7 and cards[2] - 4 == cards[6]:
                            return 'straight flush', total
                        else:
                            # flush
                            return 'flush', total

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
            return 'four of a kind', total
        if three >= 1:
            if pair >= 1 and three >= 1:
                return 'full house', total
            else:
                return 'three of a kind', total
        if pair == 1:
            return 'one pair', total
        if pair >= 2:
            return 'two pair', total

        cards = sorted([hand[_][0] for _ in range(len(hand))], reverse=True)
        if cards[0] - 4 == cards[4]:
            return 'straight', total
        elif len(cards) >= 6 and cards[1] - 4 == cards[5]:
            return 'straight', total
        elif len(cards) >= 7 and cards[2] - 4 == cards[6]:
            return 'straight', total

        return 'high card', total


if __name__ == '__main__':
    """
    player = 8p, jo, 7h, 7p, 7s, js, 5h

bot1 = ap, kp, 7h, 7p, 7s, js, 5h

bot2 = 6o, ko , 7h, 7p, 7s, js, 5h

bot3 = 2s, 3h, , 7h, 7p, 7s, js, 5h
"""

    # some testing
    from poker.Classes.Player.player import Player
    from poker.Classes.Player.bot import Bot

    p1 = Player('player')
    p1.hand = [(8, 'clubs'), (11, "diamonds"), (7, 'hearts'), (7, 'clubs'), (7, 'spades'), (11, 'spades'),
               (5, 'hearts')]
    b1 = Bot('bot1')
    b1.hand = [(14, 'clubs'), (13, 'clubs'), (7, 'hearts'), (7, 'clubs'), (7, 'spades'), (11, 'spades'),
               (5, 'hearts')]
    b2 = Bot('bot2')
    b2.hand = [(6, 'diamonds'), (13, 'diamonds'), (7, 'hearts'), (7, 'clubs'), (7, 'spades'), (11, 'spades'),
               (5, 'hearts')]
    b3 = Bot('bot3')
    b3.hand = [(2, 'spades'), (3, 'hearts'), (7, 'hearts'), (7, 'clubs'), (7, 'spades'), (11, 'spades'),
               (5, 'hearts')]

    an = WinAnalyzer([(7, 'hearts'), (7, 'clubs'), (7, 'spades'), (11, 'spades'), (5, 'hearts')])

    p1.rank = an.evaluate(p1.hand)
    b1.rank = an.evaluate(b1.hand)
    b2.rank = an.evaluate(b2.hand)
    b3.rank = an.evaluate(b3.hand)

    print(p1.rank)
    print(b1.rank)
    print(b2.rank)
    print(b3.rank)
