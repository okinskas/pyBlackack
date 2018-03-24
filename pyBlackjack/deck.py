import random
from pyBlackjack.card import Card

class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card((rank, suit)))

    def __str__(self):
        return str(self.cards)

    def remove(self, index):
        del self.cards[index] # check this is correct...

    def get_card(self):
        position = random.randint(0, len(self.cards) - 1)
        card = self.cards[position] # check this is correct
        self.remove(position)
        return card