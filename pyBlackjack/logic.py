import pyBlackjack.cards as c


def value(card):

    r = card.rank
    if r in c.FACE:
        return 10
    elif r == c.ACE:
        return 11
    else:
        return int(r)


def aggregate(hand, total=0, n=0, ace_count=0):

    if n == len(hand.cards):
        return total
    if hand.cards[n].rank == c.ACE:
        ace_count += 1

    total += value(hand.cards[n])

    if total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    return aggregate(hand.cards, total, n + 1, ace_count)


def is_blackjack(hand):

    cards = hand.cards
    if len(cards) == 2:
        ranks = [x.rank for x in cards]
        has_ace = c.ACE in ranks
        has_face = any(elem in ranks for elem in [c.KING, c.QUEEN, c.JACK])
        return has_ace and has_face
    else:
        return False


def is_bust(hand):
    return aggregate(hand) > 21


def get_winner(hand, dealer):

    p = aggregate(hand)
    d = aggregate(dealer.hand)

    if p > 21:
        return dealer
    elif d < p <= 21:
        return hand
    else:
        return hand, dealer
