
class Card(object):

    ranks = [(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),('Jack',10),('Queen',10),('King',10),('Ace',11)]
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self, card_tuple):
        self.rank, self.suit = card_tuple

    def __str__(self):
        return str(self.rank[0]) + " of " + self.suit + "."

    def get_suit(self):
        return self.suit

    def get_key(self):
        return self.rank[0]

    def get_value(self):
        return self.rank[1]

    def get_rank(self):
        return self.rank