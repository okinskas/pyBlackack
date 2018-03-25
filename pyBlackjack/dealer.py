from pyBlackjack.player import Player
import pyBlackjack.logic as logic
import pyBlackjack.cards as c

SOFT_SEVENTEEN_RULE = True


class Dealer(object):

    def __init__(self):
        self._player = Player('Dealer')
        self._hand = self._player.hand

    @property
    def name(self):
        return self._player.name

    @property
    def hand(self):
        return self._hand

    def reset(self):
        self._player.reset()  # double check this behaviour

    def choice(self):

        total = logic.aggregate(self._hand)
        is_soft_seventeen = total == 17 and c.ACE in [x.rank for x in self._hand.cards]

        if SOFT_SEVENTEEN_RULE:
            return total < 17 or is_soft_seventeen
        else:
            return total < 17
