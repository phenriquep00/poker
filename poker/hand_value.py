from collections import Counter
import deck
import player
import bots


def hand_value(obj, tbl):
    final = []
    final_suits = []
    final_values = []
    for _ in tbl.cards:
        final.append((_.suit, _.value))
    final.append((obj.hand[0].suit, obj.hand[0].value))
    final.append((obj.hand[1].suit, obj.hand[1].value))

    for suits, values in final:
        final_suits.append(suits)
        final_values.append(values)

    sorted(final)
    sorted(final_values)
    sorted(final_suits)

    # organize by suit
    c, d, h, s = [], [], [], []
    # check if they are of the same suit:
    for _ in final:
        if _[0] == 'clubs':
            c.append(_)
        elif _[0] == 'diamonds':
            d.append(_)
        elif _[0] == 'hearts':
            h.append(_)
        else:
            s.append(_)

    # check for flush possibilities:
    for _ in [c, d, h, s]:
        if len(_) >= 5:  # if True, mean there is at least a flush
            if _[0][1] == _[:-1][1]:  # there is a straight flush at least
                if _[0][1] == 10:  # Jackpot!!! there is a royal flush
                    return 'royal flush'
                else:
                    return 'straight flush'
            else:
                return 'flush'

    # check for value maching possibilities:
    pairs = []
    three = []
    four = []
    counts = Counter(final_values)
    dictionary = dict(counts)
    for k, v in dictionary.items():
        if v >= 2:  # there is at least a pair
            if v >= 3:  # at least a three of a kind
                if v == 4:  # there is a four of a kind
                    four.append(k)
                else:
                    three.append(k)
            else:
                pairs.append(k)

    if len(pairs) > 0:  # there is at least one pair
        if len(pairs) >= 2:  # there is a two pair
            return 'two pair'
        elif len(pairs) == 1 and len(three) == 1:  # there is a full house:
            return 'full house'

    if len(pairs) == 1:
        return 'pair'
    if len(three) == 1:  # there is at least a three of a kind
        return 'three of a kind'
    if len(four) == 1:  # there is a four of a kind
        return 'four of a kind'

    # check for straight
    a1 = [_ for _ in sorted(final_values)[:5]]
    a2 = [_ for _ in sorted(final_values)[1:6]]
    a3 = [_ for _ in sorted(final_values)[2:7]]
    for _ in [a1, a2, a3]:
        if (_[0] + 1) == _[1] and (_[1] + 1) == _[2] and (_[2] + 1) == _[3] and (_[3] + 1) == _[4]:
            return 'straight'
        else:
            return f'high card {sorted(final_values)[-1]}'


if __name__ == '__main__':
    player = player.Player()
    deck = deck.Deck()
    deck.shuffle()
    player.hand = deck.give_cards()

    table = bots.Table()
    table.cards = deck.give_table_cards()

    print(hand_value(obj=player, tbl=table))
