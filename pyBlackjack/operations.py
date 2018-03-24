from pyBlackjack.hand import Hand


def hit(hand, deck):
    hand.cards.append(deck.pop())


def double_down(hand, deck):
    hand.stake *= 2
    hit(hand, deck)
    hand.finished = True


def split(player):
    hand = player.hand
    if hand.cards[0].rank == hand.cards[1].rank:
        hand1 = Hand([hand.cards[0]])
        hand2 = Hand([hand.cards[1]])
        player.stack -= 10
        return hand1, hand2
    else:
        return None, None
