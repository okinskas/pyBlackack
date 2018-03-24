import pyBlackjack.cards as c


def value(card):

    r = card.rank
    if r in c.FACE:
        return 10
    elif r == c.ACE:
        return 11
    else:
        return int(r)


def is_blackjack(cards):

    if len(cards) == 2:
        ranks = [x.rank for x in cards]
        has_ace = c.ACE in ranks
        has_face = any(elem in ranks for elem in [c.KING, c.QUEEN, c.JACK])
        return has_ace and has_face
    else:
        return False


def aggregate(cards, total=0, n=0, ace_count=0):

    if n == len(cards):
        return total
    if cards[n].rank == c.ACE:
        ace_count += 1

    total += value(cards[n])

    if total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    return aggregate(cards, total, n + 1, ace_count)