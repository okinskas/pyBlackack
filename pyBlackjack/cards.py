CLUB = '♣'
DIAMOND = '♦'
HEART = '♥'
SPADE = '♠'

JACK = "J"
QUEEN = "Q"
KING = "K"
ACE = "A"

RANKS = [str(n) for n in range(2, 11)] + [JACK, QUEEN, KING, ACE]
SUITS = [CLUB, DIAMOND, HEART, SPADE]


class Card(object):

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def rank(self):
        return self._rank

    def suit(self):
        return self._suit
