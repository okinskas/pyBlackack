from pyBlackjack.hand import Hand


def hit(hand, deck):
    hand.cards.append(deck.pop())


def double_down(hand):
    hand.stake *= 2
    hand.finished = True


def split_hand(hand):
    if hand.cards[0].rank == hand.cards[1].rank:
        hand1 = Hand([hand.cards[0]])
        hand2 = Hand([hand.cards[1]])
        return hand1, hand2
    else:
        return False
