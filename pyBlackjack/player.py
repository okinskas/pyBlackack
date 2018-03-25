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

    @property
    def hand(self):
        return self._hand

    @property
    def alt(self):
        return self._alt

    def reset(self):
        self._hand = Hand()
        self._alt = None
