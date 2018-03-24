from pyBlackjack.hand import Hand
import pyBlackjack.operations as ops


class Player(object):

    def __init__(self, name):
        self._name = name
        self._stack = 100
        self._hand = Hand([])
        self._hand_alt = None

    @property
    def name(self):
        return self._name

    @property
    def stack(self):
        return self._stack

    @property
    def hand(self):
        return self._hand

    @property
    def hand_alt(self):
        return self._hand_alt

    def split(self):
        main, alt = ops.split_hand(self._hand)
        if main is not None:
            self._hand, self._hand_alt = main, alt
            self._stack -= 10

    def reset(self):
        self._hand = Hand()
        self._hand_alt = None
