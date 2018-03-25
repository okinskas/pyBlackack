from pyBlackjack.hand import Hand


class Player(object):

    def __init__(self, name):
        self._name = name
        self._stack = 100
        self._hand = Hand([])
        self._alt = None

    @property
    def name(self):
        return self._name

    @property
    def stack(self):
        return self._stack

    @stack.setter
    def stack(self, stack):
        self._stack = stack

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, hand):
        self._hand = hand

    @property
    def alt(self):
        return self._alt

    def reset(self):
        self._hand = Hand([])
        self._alt = None
