from pyBlackjack.hand import Hand


class Player(object):

    def __init__(self, name):
        self.name = name
        self.stack = 100
        self.hand_main = Hand([])
        self.hand_alt = None

    def split(self):
        main, alt = self.hand_main.split()
        if main is None:
            return False
        else:
            self.hand_main, self.hand_alt = main, alt
            return True

    def reset_hands(self):
        self.hand_main = Hand()
        self.hand_alt = None

    def has_split(self):
        return self.hand_alt is not None
