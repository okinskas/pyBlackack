from pyBlackjack.dealer import Dealer
from pyBlackjack.hand import Hand
import pyBlackjack.logic as logic


def bet(player, hand, stake=10):
    if player.stack >= stake:
        player.stack -= stake
        hand.stake += stake
        return True
    else:
        return False


def stick(hand):
    hand.finished = True
    return "stick"


def hit(hand, deck):
    hand.cards.append(deck.draw())
    if logic.is_done(hand):
        return "done"
    else:
        return True


def double_down(player, hand, deck):
    can_bet = bet(player, hand, hand.stake)

    if not can_bet:
        return False
    else:
        hit(hand, deck)
        stick(hand)
        return True


def split(player):
    hand = player.hand
    if hand.cards[0].rank == hand.cards[1].rank:
        hand1 = Hand([hand.cards[0]])
        hand2 = Hand([hand.cards[1]])
        hand1.stake = hand.stake
        can_bet = bet(player, hand2, hand.stake)

        if not can_bet:
            return False
        else:
            player.hand = hand1
            player.alt = hand2
    else:
        return False


def reward(player, dealer):
    hands = [h for h in [player.hand, player.alt] if h is not None]

    for hand in hands:
        winner = logic.get_winner(hand, dealer)

        if winner is hand:
            player.stack += winner.stake * 2
        elif winner is None:
            player.stack += hand.stake
