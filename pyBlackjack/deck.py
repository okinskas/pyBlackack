import random
import pyBlackjack.cards as c
from pyBlackjack.cards import Card


class Deck(object):

    def __init__(self):
        self._cards = []
        for suit in c.SUITS:
            for rank in c.RANKS:
                self._cards.append(Card(rank, suit))

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()
