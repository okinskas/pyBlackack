import random
import pyBlackjack.cards as Cards
from pyBlackjack.cards import Card


class Deck(object):

    def __init__(self):
        self._cards = []
        for suit in Cards.SUITS:
            for rank in Cards.RANKS:
                self._cards.append(Card(rank, suit))

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        self._cards = random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()
