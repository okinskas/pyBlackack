CLUB = '♣'
DIAMOND = '♦'
HEART = '♥'
SPADE = '♠'

JACK = "J"
QUEEN = "Q"
KING = "K"
ACE = "A"

FACE = [JACK, QUEEN, KING]
RANKS = [str(n) for n in range(2, 11)] + FACE + [ACE]
SUITS = [CLUB, DIAMOND, HEART, SPADE]


class Card(object):

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit
