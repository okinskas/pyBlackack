class Hand(object):

    def __init__(self, cards=[], stake=0):
        self._cards = cards
        self._stake = stake
        self._finished = False

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, cards):
        self._cards = cards

    @property
    def stake(self):
        return self._stake

    @stake.setter
    def stake(self, stake):
        self._stake = stake

    @property
    def finished(self):
        return self._finished

    @finished.setter
    def finished(self, has_fin):
        self._finished = has_fin
